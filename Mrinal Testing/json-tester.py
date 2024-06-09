import json
import pandas as pd
import requests

url = "https://www.walmart.ca/orchestra/graphql/browse?page=1&prg=desktop&catId=10019_6000194327370_6000194327412&sort=best_match&ps=1000&limit=500&additionalQueryParams.isMoreOptionsTileEnabled=true&additionalQueryParams.isGenAiEnabled=undefined&additionalQueryParams.view_module=undefined&searchArgs.cat_id=10019_6000194327370_6000194327412&searchArgs.prg=desktop&fitmentFieldParams=true_true_false&enableFashionTopNav=false&fetchMarquee=true&fetchSkyline=true&fetchSbaTop=false&fetchGallery=false&fetchDac=false&enablePortableFacets=true&tenant=CA_GLASS&pageType=BrowsePage&enableFacetCount=true&marketSpecificParams=\\{%22pageType%22:%22browse%22\\}&enableFlattenedFitment=false&enableMultiSave=true&fSeo=true&enableSellerType=true&enableFulfillmentTagsEnhacements=false"

headers = {
  'accept': 'application/json',
  'accept-language': 'en-CA',
  'content-type': 'application/json',
  'cookie': 'WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; auth=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; DYN_USER_ID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; ACID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; hasLocData=1; sizeID=s7n1frm118dc4htipakiitd314; vtc=WFkwM9p9B1s0mpEQxyrIOs; walmart.nearestLatLng="49.2635,-122.9331"; userSegment=50-percent; _pxvid=92192a0d-1237-11ef-b150-3fad0c304692; cartId=8f2ea269-89df-4aca-994e-3f549c989e79; _ga=GA1.1.902424607.1715721536; _gcl_au=1.1.1882684070.1715721536; localStoreInfo=eyJwb3N0YWxDb2RlIjoiVjNKMU41IiwibG9jYWxTdG9yZUlkIjoiMzAwOCIsInNlbGVjdGVkU3RvcmVJZCI6IjMwMDgiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkJVUk5BQlksIEJSSVRJU0ggQ09MVU1CSUEiLCJmdWxmaWxsbWVudFN0b3JlSWQiOiIzMDA4IiwiZnVsZmlsbG1lbnRUeXBlIjoiSU5TVE9SRV9QSUNLVVAifQo=; deliveryCatchment=3008; walmart.nearestPostalCode=V3J1N5; walmart.shippingPostalCode=V3J1N5; defaultNearestStoreId=3008; QuantumMetricUserID=df1b13baeb425052cc274724558675ef; uxcon=enforce=false&p13n=true&ads=true&createdAt=1715721533579&modifiedAt=1715721543894; dimensionData=606; _ga_N1HN887KY7=GS1.1.1715816652.3.0.1715816652.60.0.0; userAppVersion=main-1.144.1-1bcdce2-0523T2122; enableHTTPS=1; wm_route_based_language=en-CA; pxcts=5dd6edfd-243e-11ef-9ae8-82dbaa730cef; wmt.c=0; WM.USER_STATE=GUEST%7CGuest; type=GUEST%7CGuest; utmContent=utm_medium=paid_search&utm_source=google&utm_campaign=always_on&cmpid=SEM_CA_138_5565IROSQN_71700000063386362_58700005664769328&utm_id=SEM_CA_138_5565IROSQN_71700000063386362_58700005664769328&gclsrc=aw.ds&gad_source=1&gclid=CjwKCAjw34qzBhBmEiwAOUQcF9yWF_E29bWJIjs1DyRTgXtSjzN-J6z0o9JyTcvTSR1Bt2_yMQ-jehoCLXUQAvD_BwE&gclsrc=aw.ds; bstc=Z9VeMvs8MTKMtXm1pb3Gkk; xpa=26diC|2ccV5|4G26Z|4_row|5qeCE|BQ06w|FC6Rc|HwipV|JRzQo|M4aON|NOu94|Qishr|RZX3G|T3Qaq|X18Qx|acQch|bByzn|cU-uC|cfHP2|crfGA|e_PBT|f8NJH|gGsp-|h-wXP|rpnr6|s368N|wOXM5|z6fT8; exp-ck=26diC12ccV514G26Z14_row15qeCE1BQ06w1JRzQo1M4aON1NOu941Qishr1RZX3G1acQch1bByzn1cU-uC1e_PBT1f8NJH1rpnr61s368N1z6fT81; cadpweb=true; ak_bmsc=DAB492BBC6DB2101320A02AA55570674~000000000000000000000000000000~YAAQOug3Fxo377qPAQAAlUjZ9Bin16W3Z6kAYVH4UNmmbv8r+XkfGVjSfIOAcKBfzh9VUoKWlAIS0ACS6ydyJKlgzDARna/aV0O3Uid8lQ4z2fuyOAC9z8Zm3KCoSermTxWrqAhVVLzynyTm3ISPwdA446iPvVPyrsL7u0sA/UH46ESeG2TTDvoMWWuTKAVsgHfLgdAKGwYVcH4Nc/2zywkpT7mEAdxzr/cV+o5PiyYHa2Hjm/EiZdJS5hN3VGuIfXf0NOqiwXcEC3gVw09FoTaHuegmnlx3x/KMRIq5fvsXfdKe4DR8HxRcSBs9Mt4FCZI9hno0UU5a4dtKR4tNPjO/wXmuXrYwk5wOMItk8J0WMNWkfewRktaXe59mLErLQKQWgtYqcTQr; _astc=08ebdc51852765c14c4a6db1bac26f6a; _gcl_aw=GCL.1717799832.CjwKCAjw34qzBhBmEiwAOUQcF9yWF_E29bWJIjs1DyRTgXtSjzN-J6z0o9JyTcvTSR1Bt2_yMQ-jehoCLXUQAvD_BwE; _gcl_dc=GCL.1717799832.CjwKCAjw34qzBhBmEiwAOUQcF9yWF_E29bWJIjs1DyRTgXtSjzN-J6z0o9JyTcvTSR1Bt2_yMQ-jehoCLXUQAvD_BwE; _gcl_gs=2.1.k1$i1717799830; xpm=1%2B1717799831%2BWFkwM9p9B1s0mpEQxyrIOs~%2B0; QuantumMetricSessionID=bd4f1dd118d70f643796279bcc7af245; locDataV3=eyJwaWNrdXBTdG9yZSI6eyJhZGRyZXNzTGluZU9uZSI6Ijk4NTUgQXVzdGluIFJkIiwiY2l0eSI6IkJ1cm5hYnkiLCJzdGF0ZU9yUHJvdmluY2VDb2RlIjoiQkMiLCJjb3VudHJ5Q29kZSI6IkNBIiwicG9zdGFsQ29kZSI6IlYzSiAxTjUiLCJzdG9yZUlkIjoiMzAwOCIsImRpc3BsYXlOYW1lIjoiQlVSTkFCWSwgQlJJVElTSCBDT0xVTUJJQSIsImdlb1BvaW50Ijp7ImxhdGl0dWRlIjo0OS4yNDkwMjksImxvbmdpdHVkZSI6LTEyMi44OTU1OTh9LCJhY2Nlc3NQb2ludElkIjoiYmM5YjE0YmEtMjc5Yi00NTZjLTg5MTctZGYwZGJhOTU3MGE2IiwiZnVsZmlsbG1lbnRTdG9yZUlkIjoiMzAwOCIsInByaWNpbmdTdG9yZUlkIjoiMzAwOCIsImZ1bGZpbGxtZW50T3B0aW9uIjoiUElDS1VQIiwiZnVsZmlsbG1lbnRUeXBlIjoiSU5TVE9SRV9QSUNLVVAifSwic2hpcHBpbmciOnsicG9zdGFsQ29kZSI6IlYzSiAxTjUiLCJjaXR5IjoiQnVybmFieSIsInN0YXRlT3JQcm92aW5jZUNvZGUiOiJCQyIsImNvdW50cnlDb2RlIjoiQ0EiLCJsYXRpdHVkZSI6NDkuMjQ5MDI5LCJsb25naXR1ZGUiOi0xMjIuODk1NTk4LCJpc0dpZnRBZGRyZXNzIjpmYWxzZX0sImludGVudCI6IlBJQ0tVUCIsImlzRXhwbGljaXRJbnRlbnQiOmZhbHNlLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NzE4YTFlZjktMmQ1OC00YmRhLWE3ZGEtZmM2NDYzNWYwZjRhIn0%3D; adblocked=true; _px3=0c3904e55b549f084ca48730e5536e6b7577decefbc04b182fc3b1d43ae39d4d:YZO5tP8r9kP3JIj783wQnEEe9PfC45iXv7+TzLFbPxeExLHgQDn48D6bWk81zDsNFTOHgN69hYTbGdNML66Kig==:1000:l0eDhf1C4AXsbsZMXJ6jwulFFhN4vQlNBur2gxj7/iKb8dUZoQMfZYvn1y2ySV8oO5bUgVaUmvhk1QzfvKroVjwyau00bi+F+T++cCZNX/FHIyuNhO6DYZhQ3yY0gHyyfJ3IbcIEDwxaM0cYZE45U3qiu4ccvXpOMMQ39L3vyFYFz7fO7u3sUaQW/uWO5XV7JQXrtveUXf8E981DD/l2/PvZONwckBXsP9IX+IXFEAI=; _pxde=b738788a15db757a9a1962b9573f0a7e9d049ed42e4e61732f12a3ef771f82fa:eyJ0aW1lc3RhbXAiOjE3MTc4MDAwNDY5OTR9; _ga_D2P3FM55BM=GS1.1.1717799841.6.1.1717800109.59.0.1542885796; TS010110a1=01620dc0aaeeee6f28a7f58237956fbc1294f5352b6be97771dac6dc2d29d54d61effea7f9e18b8891acd42f83a61fa4bb42954b2f; TS01ea8d4c=01620dc0aaeeee6f28a7f58237956fbc1294f5352b6be97771dac6dc2d29d54d61effea7f9e18b8891acd42f83a61fa4bb42954b2f; TS0180da25=01620dc0aaeeee6f28a7f58237956fbc1294f5352b6be97771dac6dc2d29d54d61effea7f9e18b8891acd42f83a61fa4bb42954b2f; seqnum=31; TSe62c5f0d027=08e0dd7c7bab200030a2b161c515fc54540da2fd44ec4c9d6ce2dd70262ef75d18fedb64f0675a2f086df506bd113000b40ed8c48320dee8dbe37945a8ad7172a156749c7eb399b2b4d46dfada81c6f5922680b8342e9f7ae6e308886654f45d; bm_sv=E3B67A867280A3E6DA65850E46B9B5D7~YAAQOug3FzdW77qPAQAAO+Td9BhHaF5SCkQmPBb98FI3rusNmYINV37WyldQmoLkv1X+LB/TUBeP55fqmlRLGap5WijshtohxW7cjdYn8MW9pOv8EiG63Mo5cSPO8HsCBut9mnZN7TAUbcXrohpOcJ7w0kelQa1ps6NX+DF5mMrVPZaGfUlYGa8BWgxufr0agUuQT3qg06XNtJONNiqFq7bbXci5EKy/cDd9NcneIMDLAHsTDvkd/HPRnAbqo9EwSQ==~1; ACID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; TS0180da25=01aea242371b53703d0e179834b85cf1fbc9650b9fe942f320cadd7546e667e6c9a808d6422557ad19da38c65f916586495196cd0f; TS01ea8d4c=01aea242371b53703d0e179834b85cf1fbc9650b9fe942f320cadd7546e667e6c9a808d6422557ad19da38c65f916586495196cd0f; bm_sv=E3B67A867280A3E6DA65850E46B9B5D7~YAAQjpUeuJQbC/KPAQAA/Q0e9RiFBpvF469fYAOYzTiQf59TxpjWtpUFGMRtA+0G+tw5Bz4DzNBLgAyFU0EbUksVnOgcW1wI19z/chPwTwBMxtDhCRxrlW0MgMQBih3TlPYdMHGeiN+fyQYdloGkD/KaQpGZNJ775CkNNumkEupKVkqsAd14k6bR+w81F9CVHhOU5tyEuPUYJyJHiJZU08BgVPmc0IEl3vEvTH/wi812aj+n6Fnry7zT+1iRao4uDg==~1; bstc=Z9VeMvs8MTKMtXm1pb3Gkk; exp-ck=26diC12ccV514G26Z14_row15qeCE1BQ06w1JRzQo1M4aON1NOu941Qishr1RZX3G1acQch1bByzn1cU-uC1e_PBT1f8NJH1rpnr61s368N1z6fT81; seqnum=32; vtc=WFkwM9p9B1s0mpEQxyrIOs; xpa=26diC|2ccV5|4G26Z|4_row|5qeCE|BQ06w|FC6Rc|HwipV|JRzQo|M4aON|NOu94|Qishr|RZX3G|T3Qaq|X18Qx|acQch|bByzn|cU-uC|cfHP2|crfGA|e_PBT|f8NJH|gGsp-|h-wXP|rpnr6|s368N|wOXM5|z6fT8; xpm=1%2B1717804274%2BWFkwM9p9B1s0mpEQxyrIOs~%2B0; DYN_USER_ID=718a1ef9-2d58-4bda-a7da-fc64635f0f4a; TS010110a1=01aea242371b53703d0e179834b85cf1fbc9650b9fe942f320cadd7546e667e6c9a808d6422557ad19da38c65f916586495196cd0f; TSe62c5f0d027=08c5adaf41ab2000ef184a7f7ef3529caebd81fab0d1e18822f492afbdb64a14979aceb6b01552a30896be9c701130004af006e07c12d4d5f053199bf6dcc581d8eb8e32d46612cb0d541218d12cc8150531157b26c31d04e0576add553e702a; WM.USER_STATE=GUEST%7CGuest; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; auth=MTAyOTYyMDE4KqGTkuPFfCyVk1vZvlcRLvdpQc1sbpJh610%2F7rWfa9Kkz2nS%2FfDjYOZhd7MKzX7S5VnNVRF%2FyWNFLBh2OX%2BnmMkKFIaWFx7qCAjONrBTINxkUuLAruBU8ZNMIyG74mAVj8OFN4dileb20bpDLeCIlSFd%2FHsc7bnSe4%2BTLU2zbj1c8g6jBX98eONymLe%2FQflJOeIk%2FezgusOuZk1VmyRO%2BjionjZo6gS0D6lTYBOzAIDb%2FSoGFgAYL9DGZ8K45WCXJ0tmvH1FCaN9tZDh4SCrHY93iwUvNU0Xug0UlG2zBW2wuDNPzxlcMmyE8nPV0iP8mksdCdFIiV%2FrnBHch%2FMLETzdC3v6TDOOUY7CQELxPeF6h6SGjnV4LSevqesRYxFQV9rpudaVAPD0sKTOqPD3nEr1eX9YGQ0laieVMoEr348%3D; type=GUEST%7CGuest',
  'device_profile_ref_id': 'ow0giX7aWdoRuMk9DLmcgyTir5Cbrgkgczn0',
  'dnt': '1',
  'downlink': '10',
  'dpr': '1.5',
  'origin': 'https://www.walmart.ca',
  'priority': 'u=1, i',
  'referer': 'https://www.walmart.ca/en/browse/grocery/fruits-vegetables/10019_6000194327370_6000194327412?page=2',
  'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-700397d15693d042e2fd70ca7c2f13a1-fc163b7af0541b87-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.ca/en/browse/grocery/fruits-vegetables/10019_6000194327370_6000194327412?page=2',
  'wm_qos.correlation_id': 'kStB6hOmNBn6ustlfrOXTR04eCxKUbFYoKtm',
  'x-apollo-operation-name': 'Browse',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-CA',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'kStB6hOmNBn6ustlfrOXTR04eCxKUbFYoKtm',
  'x-o-gql-query': 'query Browse',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.144.1-1bcdce2-0523T2122',
  'x-o-segment': 'oaoh'
}

r = requests.request("POST",url,headers=headers)
data = json.loads(r.text)
df = pd.json_normalize(data['data'])
print(df.head())