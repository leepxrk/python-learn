import requests
 
def main():
	base = input("First Currency: ")
	other = input("Second Currency: ")
	access_key = "dd44405658a1e71fd1d896a14a76f32d"
	res_b = requests.get("http://data.fixer.io/api/latest",
						params={"access_key": access_key, "base": "EUR", "symbols": base})
	res_o = requests.get("http://data.fixer.io/api/latest",
						params={"access_key": access_key, "base": "EUR", "symbols": other})
	if res_b.status_code != 200 or res_o.status_code != 200:
		raise Exception("ERROR: API request unsuccessful.")
	data_b = res_b.json()
	data_o = res_o.json()
	rate_b = data_b["rates"][base]
	rate_o = data_o["rates"][other]
	rate = round((rate_o / rate_b), 2)
	print(f"1 {base} is equal to {rate} {other}")	
 
if __name__ == "__main__":
	main()
