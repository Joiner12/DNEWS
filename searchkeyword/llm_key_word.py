import yaml
import os
from openai import OpenAI

config_path = os.path.join(os.path.dirname(
    __file__), '..', 'config', 'config.yaml')
print(config_path)
with open(config_path, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
# 创建OpenAI客户端
client = OpenAI(api_key=config['API_KEY'],
                base_url="https://api.siliconflow.cn/v1")

keyword_weights = {"高市早苗": 0.5, "台湾": 0.3, "政治": 0.2}

# 将关键词及权重转换为适合B站搜索的优化关键词组合


def generate_optimized_bilibili_keywords(keyword_weights):
    """
    使用LLM根据关键词及权重生成适合B站搜索的优化关键词组合

    Args:
        keyword_weights (dict): 关键词及其权重的字典

    Returns:
        str: 优化后的B站搜索关键词
    """
    # 构建提示词
    keywords_desc = []
    for keyword, weight in keyword_weights.items():
        keywords_desc.append(f'"{keyword}"(权重:{weight})')

    keywords_text = "、".join(keywords_desc)
    prompt_system = "你是一个专业的视频搜索优化师，擅长根据给定关键词生成最适合的搜索词组合。"
    prompt_user = f"""关键词及权重：{keywords_text}

要求：
1. 根据权重确定关键词的重要性，权重高的关键词需要重点考虑
2. 生成适合在B站搜索的相关关键词组合
3. 考虑B站用户的搜索习惯和热门词汇
4. 结合当前时事和热点话题
5. 输出一个可以直接用于B站搜索的关键词字符串，关键词之间用空格分隔
6. 不要添加任何解释或其他文字，只输出关键词组合

请输出优化后的B站搜索关键词：
"""

    # 调用LLM生成优化的关键词组合
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user},
        ],
        temperature=0.7,
        max_tokens=200,
        stream=False
    )

    # 提取生成的关键词
    optimized_keywords = response.choices[0].message.content.strip()
    return optimized_keywords


# 生成优化的B站搜索关键词
optimized_search_keywords = generate_optimized_bilibili_keywords(
    keyword_weights)
print(f"优化后的B站搜索关键词: {optimized_search_keywords}")

# 使用优化后的关键词进行实际搜索（这里只是演示）
print(f"\n可以使用以下关键词在B站进行搜索:")
print(optimized_search_keywords)
