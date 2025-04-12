import logging
import requests
from requests.auth import HTTPBasicAuth
import itertools
import time
from typing import Dict, List, Optional

# 配置日志系统
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('alpha_generator.log'),
        logging.StreamHandler()
    ]
)

# 认证信息
USERNAME = "513923907@qq.com"
PASSWORD = "888888qq"

# 初始化全局会话
session = requests.Session()
session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
response = session.post('https://api.worldquantbrain.com/authentication')
response.raise_for_status()  # 确保认证成功
# API速率限制配置
RATE_LIMIT_BUFFER = 5  # 安全缓冲时间（秒）
MAX_RETRIES = 3
def generate_expression_templates(fields):
    """
    根据输入的字段列表生成表达式模板和推荐参数配置。
    返回一个包含多个配置字典的列表，每个字典对应一个表达式及其推荐参数设置。
    """
    cats = categorize_fields(fields)
    configs = []
    # --- 三字段表达式模板 1: (x/(y+ε)) - z ---
    if len(fields) >= 3:
        # 选择x, y, z
        x1 = None;
        y1 = None;
        z1 = None
        # 优先用成长/估值/预期字段作为x1
        if cats['growth']:
            x1 = cats['growth'][0]
        elif cats['valuation']:
            x1 = cats['valuation'][0]
        elif cats['expectation']:
            x1 = cats['expectation'][0]
        else:
            x1 = fields[0]
        # 优先用波动率或市场字段作为y1（时间序列变化较快的变量）
        if cats['vol']:
            y1 = cats['vol'][0]
        elif cats['market']:
            y1 = cats['market'][0]
        elif cats['expectation'] and cats['expectation'][0] != x1:
            y1 = cats['expectation'][0]
        elif cats['valuation'] and cats['valuation'][0] != x1:
            y1 = cats['valuation'][0]
        elif cats['growth'] and cats['growth'][0] != x1:
            y1 = cats['growth'][0]
        if not y1:
            # 若仍未选出y1，则选列表中与x1不同的第一个字段
            for f in fields:
                if f != x1:
                    y1 = f
                    break
        # 优先用市值字段或其它正值字段作为z1（分母/减数）
        if cats['cap']:
            z1 = cats['cap'][0]
        else:
            for f in cats['market']:
                lowf = f.lower()
                if 'price' in lowf or 'close' in lowf or 'volume' in lowf:
                    z1 = f
                    break
            if not z1 and cats['market']:
                z1 = cats['market'][0]
        if not z1:
            if cats['vol'] and cats['vol'][0] != y1:
                z1 = cats['vol'][0]
            elif cats['valuation'] and cats['valuation'][0] not in [x1, y1]:
                z1 = cats['valuation'][0]
            elif cats['growth'] and cats['growth'][0] not in [x1, y1]:
                z1 = cats['growth'][0]
            elif cats['expectation'] and cats['expectation'][0] not in [x1, y1]:
                z1 = cats['expectation'][0]
        if not z1:
            # 仍未选出则取一个不等于x1或y1的字段
            for f in fields:
                if f != x1 and f != y1:
                    z1 = f
                    break
        expr = f"({x1} / ({y1} + power(10,-6))) - {z1}"
        configs.append({
            'expression': expr,
            'decay': [0, 3, 5],
            'truncation': [0.02, 0.05],
            'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
            'pasteurization': 'ON',
            'nanHandling': 'ON',
            'delay': 1
        })
        # --- 三字段表达式模板 2: x * ts_rank(y,5) / (z+ε) ---
        # 尽量选与上式不同的字段组合
        x2 = None;
        y2 = None;
        z2 = None
        if cats['expectation'] and cats['expectation'][0] not in [x1, y1, z1]:
            x2 = cats['expectation'][0]
        elif cats['valuation'] and cats['valuation'][0] not in [x1, y1, z1]:
            x2 = cats['valuation'][0]
        elif cats['growth'] and cats['growth'][0] not in [x1, y1, z1]:
            x2 = cats['growth'][0]
        else:
            # 如所有基本面类字段均已用过，则仍用x1（避免为空）
            x2 = x1
        if cats['market']:
            for f in cats['market']:
                if f != y1:  # 避免重复y1
                    y2 = f
                    break
            if not y2:
                y2 = cats['market'][0]
        if not y2 and cats['vol'] and cats['vol'][0] != y1:
            y2 = cats['vol'][0]
        if not y2 and cats['expectation'] and cats['expectation'][0] not in [x2, y1]:
            y2 = cats['expectation'][0]
        if not y2:
            for f in fields:
                if f != x2:
                    y2 = f
                    break
        if cats['cap'] and cats['cap'][0] not in [x2, y2, x1, y1, z1]:
            z2 = cats['cap'][0]
        if not z2:
            if cats['expectation'] and cats['expectation'][0] not in [x2, y2, x1, y1]:
                z2 = cats['expectation'][0]
            elif cats['valuation'] and cats['valuation'][0] not in [x2, y2, x1, y1]:
                z2 = cats['valuation'][0]
            elif cats['growth'] and cats['growth'][0] not in [x2, y2, x1, y1]:
                z2 = cats['growth'][0]
            elif cats['vol'] and cats['vol'][0] not in [x2, y2, x1, y1]:
                z2 = cats['vol'][0]
            elif cats['market'] and cats['market'][0] not in [x2, y2, x1, y1]:
                z2 = cats['market'][0]
        if not z2:
            for f in fields:
                if f != x2 and f != y2:
                    z2 = f
                    break
        expr = f"{x2} * ts_rank({y2}, 5) / ({z2} + power(10,-6))"
        configs.append({
            'expression': expr,
            'decay': [0, 3, 5],
            'truncation': [0.02, 0.05],
            'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
            'pasteurization': 'ON',
            'nanHandling': 'ON',
            'delay': 1
        })
    # --- 两字段表达式模板 1: rank(x - group_mean(y, sector)) ---
    if len(fields) >= 2:
        a = None;
        b = None
        # 优先选用基本面字段与另一字段组合做行业均值剔除
        if cats['growth'] and cats['valuation']:
            a = cats['growth'][0];
            b = cats['valuation'][0]
        elif cats['growth'] and cats['expectation']:
            a = cats['growth'][0];
            b = cats['expectation'][0]
        elif cats['valuation'] and cats['expectation']:
            a = cats['valuation'][0];
            b = cats['expectation'][0]
        else:
            a = fields[0]
            for f in fields[1:]:
                if f != a:
                    b = f
                    break
            if b is None and len(fields) > 1:
                b = fields[1]
        if a and b:
            expr = f"rank({a} - group_mean({b}, sector))"
            configs.append({
                'expression': expr,
                'decay': [0, 3, 5],
                'truncation': [0.02, 0.05],
                'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
                'pasteurization': 'ON',
                'nanHandling': 'ON',
                'delay': 1
            })
    # --- 两字段表达式模板 2: 波动率字段的平滑/分位数处理 ---
    if cats['vol']:
        vol_field = cats['vol'][0]
        other_fields = [f for f in fields if f != vol_field]
        if other_fields:
            # 分位数差分: quantile(vol, n) - other
            other1 = None
            for f in other_fields:
                fl = f.lower()
                if ('growth' in fl or 'increase' in fl or 'yoy' in fl or 'qoq' in fl or
                        'pe' in fl or 'pb' in fl or 'expect' in fl):
                    other1 = f
                    break
            if not other1:
                other1 = other_fields[0]
            expr = f"quantile({vol_field}, 5) - {other1}"
            configs.append({
                'expression': expr,
                'decay': [0, 3, 5],
                'truncation': [0.02, 0.05],
                'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
                'pasteurization': 'ON',
                'nanHandling': 'ON',
                'delay': 1
            })
            # 平滑比值: ts_mean(vol, n) / (other + ε)
            if len(other_fields) > 1:
                other2 = None
                for f in other_fields:
                    if f != other1:
                        other2 = f
                        break
                if not other2:
                    other2 = other_fields[1]
                expr = f"ts_mean({vol_field}, 3) / ({other2} + power(10,-6))"
                configs.append({
                    'expression': expr,
                    'decay': [0, 3, 5],
                    'truncation': [0.02, 0.05],
                    'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
                    'pasteurization': 'ON',
                    'nanHandling': 'ON',
                    'delay': 1
                })
    # --- 两字段表达式模板 3: 成长/估值字段的比值或差值 ---
    fund_fields = cats['growth'] + cats['valuation']
    if len(fund_fields) >= 2:
        a = fund_fields[0];
        b = fund_fields[1]
        expr = f"{a} / ({b} + power(10,-6))"
        configs.append({
            'expression': expr,
            'decay': [0, 3, 5],
            'truncation': [0.02, 0.05],
            'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
            'pasteurization': 'ON',
            'nanHandling': 'ON',
            'delay': 1
        })
    elif len(fund_fields) == 1:
        a = fund_fields[0]
        b = None
        # 若只有一个成长/估值字段，用其他类别字段与其组合
        if cats['expectation']:
            b = cats['expectation'][0]
        elif cats['market']:
            b = cats['market'][0]
        elif cats['cap']:
            b = cats['cap'][0]
        elif cats['vol']:
            b = cats['vol'][0]
        elif cats['other']:
            b = cats['other'][0]
        if b:
            bl = b.lower()
            if 'price' in bl or 'close' in bl or 'cap' in bl or 'volume' in bl:
                expr = f"{a} / ({b} + power(10,-6))"
            else:
                expr = f"{a} - {b}"
            configs.append({
                'expression': expr,
                'decay': [0, 3, 5],
                'truncation': [0.02, 0.05],
                'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
                'pasteurization': 'ON',
                'nanHandling': 'ON',
                'delay': 1
            })
    # --- 两字段表达式模板 4: 市值归一化 ---
    if cats['cap']:
        cap_field = cats['cap'][0]
        a = None
        # 用预期或基本面字段除以市值
        if cats['expectation']:
            a = cats['expectation'][0]
        elif cats['growth']:
            a = cats['growth'][0]
        elif cats['valuation']:
            a = cats['valuation'][0]
        elif cats['market']:
            # 若有成交量字段，用成交量否则用第一个市场字段
            volm = None
            for f in cats['market']:
                if 'volume' in f.lower() or 'turnover' in f.lower():
                    volm = f
                    break
            a = volm if volm else cats['market'][0]
        elif cats['vol']:
            a = cats['vol'][0]
        elif cats['other']:
            a = cats['other'][0]
        if a and a != cap_field:
            expr = f"{a} / ({cap_field} + power(10,-6))"
            configs.append({
                'expression': expr,
                'decay': [0, 3, 5],
                'truncation': [0.02, 0.05],
                'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
                'pasteurization': 'ON',
                'nanHandling': 'ON',
                'delay': 1
            })
    # --- 两字段表达式模板 5: 预期与市场变化差 ---
    if cats['expectation'] and cats['market']:
        exp_field = cats['expectation'][0]
        m_field = None
        # 优先用包含'ret'（收益）或'price'的市场字段表示价格变动
        for f in cats['market']:
            low = f.lower()
            if 'ret' in low:
                m_field = f
                break
            if 'price' in low or 'close' in low:
                m_field = f
                break
        if not m_field:
            m_field = cats['market'][0]
        expr = f"ts_delta({exp_field}, 5) - ts_delta({m_field}, 5)"
        configs.append({
            'expression': expr,
            'decay': [0, 3, 5],
            'truncation': [0.02, 0.05],
            'neutralization': ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR'],
            'pasteurization': 'ON',
            'nanHandling': 'ON',
            'delay': 1
        })
    return configs


# 获取所有字段
def get_datafields(dataset_id, searchScope):
    url_template = f"https://api.worldquantbrain.com/data-fields?dataset.id={dataset_id}&instrumentType={searchScope['instrumentType']}&region={searchScope['region']}&delay={searchScope['delay']}&universe={searchScope['universe']}&limit=50&offset={{}}"
    fields = []
    offset = 0

    while True:
        try:
            # 添加请求重试机制
            for attempt in range(3):
                try:
                    response = session.get(url_template.format(offset), timeout=15)
                    response.raise_for_status()

                    # 检查内容类型
                    content_type = response.headers.get('Content-Type', '')
                    if 'application/json' not in content_type:
                        logging.warning("异常响应类型: %s", content_type)
                        logging.debug("响应内容: %s", response.text[:200])
                        raise ValueError("非JSON响应")

                    data = response.json()
                    break
                except requests.exceptions.RequestException as e:
                    if attempt < 2:
                        wait_time = 2 ** attempt
                        logging.warning("请求失败，%ds后重试: %s", wait_time, str(e))
                        time.sleep(wait_time)
                    else:
                        raise

            # 处理分页逻辑
            current_fields = [f['id'] for f in data.get('results', []) if f['type'] == 'MATRIX']
            fields.extend(current_fields)

            if len(data.get('results', [])) < 50:
                break
            offset += 50

            # 遵守速率限制
            remaining = int(response.headers.get('X-RateLimit-Remaining', 1))
            if remaining <= 5:
                reset_time = int(response.headers.get('X-RateLimit-Reset', 60))
                print("接近速率限制，等待 %d 秒", reset_time)
                time.sleep(reset_time + 5)

        except Exception as e:
            print("获取数据字段失败: %s", str(e))
            print("错误发生时的URL: %s", url_template.format(offset))
            break

    return fields


# 字段分类函数（你的完整函数）
def categorize_fields(fields):
    """
    将字段名按特征分类：
    返回包含 'vol', 'growth', 'valuation', 'cap', 'expectation', 'market', 'other' 分组的字典
    """
    categories = {
        'vol': [],  # 波动率类
        'growth': [],  # 成长类
        'valuation': [],  # 估值类
        'cap': [],  # 市值类
        'expectation': [],  # 财务预期类
        'market': [],  # 市场交易类（价格、收益、成交量等）
        'other': []  # 其他未分类字段
    }
    for f in fields:
        fl = f.lower()
        if any(word in fl for word in ["volatility", "stddev", "std_dev", "std", "variance"]):
            categories['vol'].append(f)
        elif "volume" in fl or "turnover" in fl:
            # 成交量类也视作市场类变量
            categories['market'].append(f)
        elif any(word in fl for word in ["growth", "increase", "yoy", "qoq"]):
            categories['growth'].append(f)
        elif any(word in fl for word in ["pe", "p/e", "pb", "p/b", "valuation", "yield", "rate"]):
            # 包含PE、PB、收益率、估值等关键词
            categories['valuation'].append(f)
        elif "cap" in fl:
            categories['cap'].append(f)
        elif any(word in fl for word in ["forecast", "expect", "eps_fy", "analyst", "consensus", "guidance"]):
            categories['expectation'].append(f)
        elif any(word in fl for word in ["price", "close", "open", "high", "low", "return", "ret", "vwap"]):
            categories['market'].append(f)
        else:
            categories['other'].append(f)
    return categories

def handle_rate_limits(response: requests.Response) -> None:
    """处理速率限制头信息"""
    if 'X-RateLimit-Remaining' in response.headers:
        remaining = int(response.headers['X-RateLimit-Remaining'])
        if remaining <= 5:
            reset_time = int(response.headers.get('X-RateLimit-Reset', 60))
            logging.warning(f"接近速率限制，剩余 {remaining} 次请求，等待 {reset_time} 秒")
            time.sleep(reset_time + RATE_LIMIT_BUFFER)


def api_request_with_retry(
        method: str,
        url: str,
        max_retries: int = MAX_RETRIES,
        **kwargs
) -> Optional[requests.Response]:
    """带重试和速率控制的API请求"""
    retries = 0
    while retries < max_retries:
        try:
            response = session.request(method, url, timeout=30, **kwargs)
            response.raise_for_status()

            # 处理速率限制
            handle_rate_limits(response)
            return response

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                reset_time = int(e.response.headers.get('Retry-After', 60))
                logging.warning(f"速率限制触发，等待 {reset_time} 秒")
                time.sleep(reset_time + RATE_LIMIT_BUFFER)
                retries += 1
            else:
                logging.error(f"HTTP错误: {str(e)}")
                break
        except requests.exceptions.RequestException as e:
            logging.error(f"请求失败: {str(e)}，重试 {retries + 1}/{max_retries}")
            retries += 1
            time.sleep(2 ** retries)  # 指数退避

    logging.error(f"请求失败超过最大重试次数 {max_retries}")
    return None


# 修改后的submit_simulation函数
def submit_simulation(expr: str, neutralization: str, decay: int, truncation: float) -> Optional[str]:
    """提交模拟任务（带增强错误处理）"""
    simulation_data = {
        "type": "REGULAR",
        "settings": {
            "instrumentType": "EQUITY",
            "region": "USA",
            "universe": "TOP3000",
            "delay": 1,
            "decay": decay,
            "neutralization": neutralization,
            "truncation": truncation,
            "pasteurization": "ON",
            "unitHandling": "VERIFY",
            "nanHandling": "ON",
            "language": "FASTEXPR",
            "visualization": False
        },
        "regular": expr
    }

    response = api_request_with_retry(
        'POST',
        'https://api.worldquantbrain.com/simulations',
        json=simulation_data
    )

    if response and response.status_code == 201:
        return response.headers.get('Location')
    return None


# 优化后的get_simulation_result函数
def get_simulation_result(sim_url: str, timeout: int = 600) -> Optional[Dict]:
    """获取模拟结果（带进度监控）"""
    start_time = time.time()
    poll_interval = 5  # 初始轮询间隔

    while time.time() - start_time < timeout:
        response = api_request_with_retry('GET', sim_url)
        if not response:
            return None

        try:
            data = response.json()
            status = data.get('status')

            if status == 'COMPLETE':
                logging.info(f"任务完成: {sim_url}")
                return data

            elif status in ['PENDING', 'PROCESSING']:
                progress = data.get('progress', 0)
                retry_after = float(response.headers.get('Retry-After', poll_interval))
                logging.info(f"处理中 - 进度: {progress:.1%}，等待 {retry_after} 秒")
                time.sleep(retry_after)
                poll_interval = min(poll_interval * 1.5, 30)  # 动态增加轮询间隔

            else:
                logging.error(f"未知状态: {status}，响应: {data}")
                return None

        except requests.exceptions.JSONDecodeError:
            logging.error(f"响应解析失败，原始内容: {response.text[:200]}")
            return None

    logging.error(f"监控超时 ({timeout} 秒)")
    return None


# 优化后的main函数
def main():
    """主执行流程"""
    try:
        # 认证检查
        auth_response = api_request_with_retry(
            'POST',
            'https://api.worldquantbrain.com/authentication'
        )
        if not auth_response:
            logging.error("认证失败")
            return

        search_scope = {
            'region': 'USA',
            'delay': '1',
            'universe': 'TOP3000',
            'instrumentType': 'EQUITY'
        }

        dataset_ids = ['fundamental6', 'analyst4', 'pv1']
        param_combinations = itertools.product(
            ['SUBINDUSTRY', 'INDUSTRY'],
            [0, 3],
            [0.02, 0.05]
        )

        for dataset_id in dataset_ids:
            fields = get_datafields(dataset_id, search_scope)
            logging.info(f"数据集 {dataset_id} 获取到 {len(fields)} 个字段")

            if not fields:
                logging.warning(f"数据集 {dataset_id} 无可用字段，跳过")
                continue

            configs = generate_expression_templates(fields)

            for config in configs:
                expr = config['expression']
                logging.info(f"生成表达式: {expr}")

                for neu, dec, tru in param_combinations:
                    sim_url = submit_simulation(expr, neu, dec, tru)
                    if not sim_url:
                        continue

                    logging.info(f"已提交任务: {sim_url}")
                    result = get_simulation_result(sim_url)

                    if result and 'alpha' in result:
                        ir = result['alpha'].get('ir', 'N/A')
                        logging.info(f"成功! IR: {ir}")
                    else:
                        logging.warning("回测失败")

                    time.sleep(1)  # 请求间隔保护

    except KeyboardInterrupt:
        logging.info("用户中断执行")
    except Exception as e:
        logging.error(f"未处理异常: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()