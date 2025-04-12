import requests
from requests.auth import HTTPBasicAuth
import itertools
import pandas as pd
import time

# 填入你的账号密码
USERNAME = "513923907@qq.com"
PASSWORD = "888888qq"

# 初始化Session并登录WorldQuant
session = requests.session()
session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
session.post('https://api.worldquantbrain.com/authentication')

# 修改后的 URLs定义（limit改为50）
DATASETS_URL = "https://api.worldquantbrain.com/data-sets?delay=1&instrumentType=EQUITY&limit=50&offset={}&region=USA&universe=TOP3000"
FIELDS_URL = "https://api.worldquantbrain.com/data-fields?dataset.id={}&delay=1&instrumentType=EQUITY&limit=50&offset={}&region=USA&universe=TOP3000"


# 获取全部数据集
def get_all_datasets():
    datasets = []
    offset = 0
    while True:
        res = session.get(DATASETS_URL.format(offset)).json()
        if not isinstance(res, dict) or 'results' not in res:
            print("获取的数据集格式异常：", res)
            break
        datasets.extend(res['results'])
        if len(res['results']) < 50:
            break
        offset += 50
    return datasets




def get_fields_for_dataset(dataset_id):
    fields = []
    offset = 0
    while True:
        res = session.get(FIELDS_URL.format(dataset_id, offset)).json()
        if isinstance(res, list) and res == ['Invalid query']:
            print(f"❌数据集 {dataset_id} 查询无效，跳过该数据集")
            break
        if not isinstance(res, dict) or 'results' not in res:
            print(f"获取字段格式异常：{res}")
            break
        fields.extend(res['results'])
        if len(res['results']) < 50:
            break
        offset += 50
    matrix_fields = [f['id'] for f in fields if f.get('type') == 'MATRIX']
    return matrix_fields






# 构建复杂表达式模板
def generate_expression(f1, f2=None, group='subindustry'):
    epsilon = 0.001
    if f2:
        return f"group_rank(ts_mean(rank({f1}/({f2}+{epsilon})),5), {group})"
    else:
        return f"group_rank(zscore(ts_delta({f1}, 5)), {group})"


# 提交模拟
def submit_simulation(expr, neutralization, decay, truncation):
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
    response = session.post('https://api.worldquantbrain.com/simulations', json=simulation_data)
    return response.headers.get('Location', None)


# 获取模拟结果
def get_simulation_result(sim_url):
    while True:
        res = session.get(sim_url)
        retry = res.headers.get("Retry-After")
        if retry:
            time.sleep(float(retry))
        else:
            return res.json()


# 主程序整合所有步骤
def main():
    datasets = get_all_datasets()

    neutralizations = ['SUBINDUSTRY', 'INDUSTRY', 'SECTOR']
    decays = [0, 3, 5]
    truncations = [0.02, 0.05]

    for dataset in datasets:
        # 注意修改这里
        dataset_id = dataset['id']  # 重要！确保取出id字符串
        fields = get_fields_for_dataset(dataset_id)
        if not fields:
            continue  # 跳过无效或无字段数据集
        # 单字段表达式
        for field in fields:
            expr = generate_expression(field)
            for neu, dec, tru in itertools.product(neutralizations, decays, truncations):
                sim_url = submit_simulation(expr, neu, dec, tru)
                if sim_url:
                    result = get_simulation_result(sim_url)
                    sharpe = result.get('is', {}).get('sharpe', 0)
                    turnover = result.get('is', {}).get('turnover', 100)
                    fitness = result.get('is', {}).get('fitness', 0)
                    if sharpe > 1.25 and 1 < turnover < 70 and fitness >= 1:
                        print(f"✅通过: {expr}, Sharpe={sharpe:.2f}, Turnover={turnover:.2f}, Fitness={fitness:.2f}")
                    else:
                        print(f"❌未通过: {expr}")
                else:
                    print(f"⚠️提交失败: {expr}")

        # 双字段表达式
        for f1, f2 in itertools.combinations(fields, 2):
            expr = generate_expression(f1, f2)
            for neu, dec, tru in itertools.product(neutralizations, decays, truncations):
                sim_url = submit_simulation(expr, neu, dec, tru)
                if sim_url:
                    result = get_simulation_result(sim_url)
                    print(result)



if __name__ == "__main__":
    main()

