from openai import OpenAI
import time

BASEURL = 'http://localhost:11434/v1' 
llm = OpenAI(api_key="eskfjdfhfghgsdjf", base_url=BASEURL)

messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'}  ]

def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = llm.chat.completions.create(
        model="llama3.2:3b",#deepseek-r1:latest
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content.strip('\"')

def get_stream_completion(prompt):
    messages = [{"role": "user", "content": prompt}]co
    stream = llm.chat.completions.create(
        model="llama3.2:3b",#deepseek-r1:latest
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        stream=True
    )
    text = []
    for chunk in stream:
        received_text = chunk.choices[0].delta.content
        if received_text is not None:
            text.append(received_text)
            yield received_text
            

def get_completion_from_messages(messages, temperature=0):
    response = llm.chat.completions.create(
        model="llama3.2:3b",#deepseek-r1:latest
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message.content.strip('\"')

def main():
    while True:
        prompt = input("Enter Prompt: ")

        if prompt in ("quit", "bye", "exit"):
            break

        #response = get_stream_completion(prompt=prompt)
        #for i, chunk in enumerate(response):
        #    print(chunk)

        #for line in response:
        #    print(line, end='\r', flush=True)
        #    time.sleep(0.1)
        #    print()
        messages.append({"role": "user", "content": prompt})
        response = get_completion_from_messages(messages=messages)
        messages.append({"role": "assistant", "content": response})

        #response = get_completion(prompt=prompt)
        print(f"Assistant: {response}")


if __name__ == '__main__':
   main()

