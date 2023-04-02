import streamlit as st
import openai
import config as cf
# Cài đặt thông tin model
openai.api_key=cf.API_KEY
# Hàm để gọi đến OpenAPI / Phần ChatGPT
def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(
        engine= cf.model,
        prompt = user_question,
        max_tokens = 4000,
        n = 1,
        temperature = 0.5
    )
    response_text = response.choices[0].text
    return response_text
def get_summary(ticket):
    smr='tóm tắt bài viết '
    data=[]
    post_s=[]
    t_link='./file/'+ticket+'.txt'
    with open(t_link,'r') as fp:
        sd=fp.readlines()
        data=[line.rstrip('\n') for line in sd]
    for n_link in data:
        smr_s=smr + n_link
        temp=get_response_from_chatgpt(smr_s)
        post_s.append(temp)
    return post_s
alpha=get_response_from_chatgpt('tóm tắt bài viết https://s.cafef.vn/ACB-547247/acb-nghi-quyet-hdqt-vv-cung-cap-dich-vu-chi-ho-qua-api-cho-cong-ty-tnhh-chung-khoan-acb.chn')
print(alpha)