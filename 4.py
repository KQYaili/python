import logging

import requests
from requests.auth import HTTPBasicAuth
import itertools
import time

USERNAME = "513923907@qq.com"
PASSWORD = "888888qq"

session = requests.session()
session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
response = session.post('https://api.worldquantbrain.com/authentication')
response.raise_for_status()  # 确保认证成功


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
            expr = f"rank({a} - group_mean({b},volume,sector))"
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


        except Exception as e:
            print("获取数据字段失败: %s", str(e))
            print("错误发生时的URL: %s", url_template.format(offset))
            break

    return fields


# 字段分类函数（你的完整函数）
def categorize_fields(fields):
    categories = {'vol': [], 'growth': [], 'valuation': [], 'cap': [], 'expectation': [], 'market': [], 'other': []}
    for f in fields:
        fl = f.lower()
        if any(word in fl for word in ["volatility", "stddev", "variance", "std_dev"]):
            categories['vol'].append(f)
        elif "volume" in fl or "turnover" in fl:
            categories['market'].append(f)
        elif any(word in fl for word in ["growth", "increase", "yoy", "qoq"]):
            categories['growth'].append(f)
        elif any(word in fl for word in ["pe", "pb", "valuation", "yield", "rate"]):
            categories['valuation'].append(f)
        elif "cap" in fl:
            categories['cap'].append(f)
        elif any(word in fl for word in ["forecast", "expect", "eps_fy", "analyst", "guidance", "consensus"]):
            categories['expectation'].append(f)
        elif any(word in fl for word in ["price", "close", "open", "high", "low", "return", "ret", "vwap"]):
            categories['market'].append(f)
        else:
            categories['other'].append(f)
    return categories


# 生成复杂表达式模板（你的完整函数）
# 【此处放置你的 generate_expression_templates(fields) 函数，不重复贴】

# 提交模拟函数
def submit_simulation(expr, neutralization, decay, truncation):
    print(f"提交表达式：{expr}")
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
    retries = 0
    while retries < 100:
        try:
            response = session.post(
                'https://api.worldquantbrain.com/simulations',
                json=simulation_data,
                timeout=30
            )
            print(f"提交响应状态码：{response.status_code}")

            # 成功提交
            if response.status_code == 201:
                return response.headers.get('Location')

            # 处理速率限制
            elif response.status_code == 429:
                retry_after = float(response.headers.get('Retry-After', 10))
                print(f"速率限制，等待 {retry_after} 秒后重试（剩余重试次数 {100 - retries}）")
                time.sleep(retry_after)
                retries += 1
                continue  # 关键点：重新进入循环发起新请求

            # 其他错误
            else:
                print(f"提交失败 [{response.status_code}]: {response.text[:200]}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"网络请求异常: {str(e)}")
            retries += 1
            time.sleep(2 ** retries)  # 指数退避

    print(f"超过最大重试次数 {100}")
    return None


# 获取模拟结果
def get_simulation_result(sim_url):
    """
        获取模拟结果，处理异步任务状态，直到任务完成或出错
        """
    max_attempts = 200  # 最大尝试次数，避免无限循环
    attempt = 0
    while attempt < max_attempts:
        res = session.get(sim_url)
        print(f"Response status: {res.status_code}, Content-Type: {res.headers.get('Content-Type')}")  # 调试信息

        # 检查HTTP状态码是否为200
        if res.status_code != 200:
            print(f"错误：收到状态码 {res.status_code}，响应内容：{res.text[:200]}")
            return None

        # 尝试解析JSON
        try:
            data = res.json()
        except requests.exceptions.JSONDecodeError:
            print(f"无法解析JSON，原始响应内容：{res.text[:200]}")
            return None

        # 检查任务状态
        status = data.get('status')
        print(f"任务状态：{status}")
        if status:
            return data
        else:
            # 获取等待时间，默认5秒
            print(data)
            retry_after = res.headers.get('Retry-After', 10)
            wait_time = float(retry_after)
            print(f"任务处理中，状态：{status}，等待 {wait_time} 秒后重试...")
            time.sleep(wait_time)
            attempt += 1

    print(f"超过最大尝试次数（{max_attempts}），终止重试。")
    return None


# 主函数
def main():
    searchScope = {'region': 'USA', 'delay': '1', 'universe': 'TOP3000', 'instrumentType': 'EQUITY'}

    dataset_ids = ['fundamental6', 'analyst4', 'pv1']  # 根据需要自行添加或调整
    neutralizations = ['SUBINDUSTRY', 'INDUSTRY']
    decays = [0, 3]
    truncations = [0.02, 0.05]

    for dataset_id in dataset_ids:
        fields = get_datafields(dataset_id, searchScope)

        print(f"Dataset {dataset_id} got {len(fields)} fields.")

        configs = generate_expression_templates(fields)

        for config in configs:
            expr = config['expression']
            for neu, dec, tru in itertools.product(neutralizations, decays, truncations):
                sim_url = submit_simulation(expr, neu, dec, tru)
                if not sim_url:
                    print("跳过无效的sim_url")
                    continue

                print(f"正在获取结果，URL: {sim_url}")
                result = get_simulation_result(sim_url)
                if result:
                    print(f"模拟结果：IR={result}")
                else:
                    print("获取结果失败")


if __name__ == "__main__":
    main()
