import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

with open("knowledge_list.txt", "r", encoding="utf-8") as f:
    knowledge_points = [line.strip() for line in f if line.strip()]

super_strong_prompt = """
你是一個超強電子技術教練，請用最簡單的語言從零開始教我這個知識點。
知識點: "{knowledge_point}"

請遵循以下要求：
- 每個概念用簡單例子+比喻+圖像想像解釋
- 說明常見錯誤
- 提供操作或練習建議
- 不跳過任何步驟
"""

output_file = "AI_回答收集.txt"
with open(output_file, "w", encoding="utf-8") as out_f:
    for idx, kp in enumerate(knowledge_points, start=1):
        prompt = super_strong_prompt.format(knowledge_point=kp)
        
        print(f"[{idx}/{len(knowledge_points)}] Processing: {kp} / 正在處理: {kp}")
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            answer = response['choices'][0]['message']['content']
            
            out_f.write(f"==== Knowledge Point {idx}: {kp} / 知識點 {idx}: {kp} ====\n")
            out_f.write(answer + "\n\n")
        
        except Exception as e:
            print(f"Error / 錯誤: {e}")
            out_f.write(f"==== Knowledge Point {idx}: {kp} / 知識點 {idx}: {kp} ====\n")
            out_f.write(f"Error / 錯誤: {e}\n\n")
        
print(f"Done! All responses saved to {output_file} / 完成！所有回答已保存到 {output_file}")