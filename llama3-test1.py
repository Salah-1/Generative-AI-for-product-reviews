import requests

#set keys
# Load the environment variables from the .env file. pip not availabe, so read from file instead!
from env2 import *

# API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"
API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {"Authorization": f"Bearer {token_1}"}
# sample review below ..that's long enough.
review_var1 = "First let me remind everyone that this is a $59 complete board. Belly is really attractive. First time I rode it it tracked badly to the right so I had to take the trucks apart. One was installed slightly crooked (truck not completely parallel) and the bushings were unevenly pinched. Took both off and put back on and all was well - 20 minutes with the correct tools. Took it for a 3-4 mile ride and came back with both compliments and complaints. First of all the entire perimeter of the board has a lip - turned up. Personal preference but I wasn't aware of it when I ordered and I didn't like it. Oh well - did I mention this was $59 complete? OK - so on to the more technical. After I got over the lip it was a pretty decent ride but I made some changes... I'd call the bushings medium hardness, meaning it takes a bit to turn but I liked the control. I didn't hate the wheels but the bearings sucked. I tossed on a set of 80/80 wheels for a more chill ride, and put in a pretty cheap but brand-new/respected set of REDS. The result is a REALLY comfy ride with medium quickness for less than $100. Once I'm used to the board I'll decide if I want to toss in a nicer/faster set of bearings and take on some bigger hills (likely). Can't speak to durability yet but all in all I'm happy with the purchase and would confidently check out another Ten Toes board after one of my kids steals this one - which is just a matter of time...."


# print(token_1)
# print(headers)

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
# output = query({
# 	"inputs": "What is female lion called? ",
# })

output = query({
	"inputs": f"You will be provided with text delimited by triple backticks. Let me know if its positive or negative. Also, give your answer in one sentence. ```{review_var1}``` ",
})
# output = {"inputs": f"You will be provided with text delimited by triple backticks. Let me know if its positive or negative. ```{review_var1}``` "}
print(output)