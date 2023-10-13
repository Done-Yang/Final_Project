from django.shortcuts import render, redirect
import socket
# from django.contrib import messages
import requests
import ipaddress

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def search_result(request):
    if request.method == 'GET':
        search_detial = request.GET.get('search')
        def is_host(input_str):
             try:
                host_obj = socket.gethostbyname(input_str)
                return True
             except:
                return False
        def is_ip_address(input_str):
            try:
                ip_address_obj = ipaddress.ip_address(input_str)
                return True
            except:
                return False
        if search_detial != '':
            if is_host(search_detial):
                try:
                    # Get the IP address of the host name
                    ip_address = socket.gethostbyname(search_detial)
                    
                    #request api from https://ipapi.co
                    response = requests.get(f"https://ipapi.co/{ip_address}/json/")
                    data = response.json()

                    # Get the host name and IP address of the local machine
                    local_host_name = socket.gethostname()

                    print(data)
                    rg = data['region']
                    
                    country = data['country_name']
                    country_code = data["country_code"]
                    city = data["city"]
                    latitude = data["latitude"]
                    longitude = data["longitude"]
                    country_calling_code = data["country_calling_code"]
                    org = data["org"]

                    context = {
                            "search_detial": search_detial,
                            "ip_address":ip_address,
                            "local_host":local_host_name,
                            "region": rg,
                            "country": country,
                            "country_code": country_code,
                            "city": city,
                            "latitude": latitude,
                            "longitude": longitude,
                            "country_calling_code": country_calling_code,
                            "org": org
                            }
                    return render(request, 'search_result.html', context=context)
                except:
                    # messages.warning(request, "Please, correct your IP Address!")
                    print("host")
                    context = {
                        "search_detial": search_detial,
                        "ip_address":"N/A",
                        "local_host": "N/A",
                        "region": 'N/A',
                        "country": 'N/A',
                        "country_code": 'N/A',
                        "city": 'N/A',
                        "latitude": 'N/A',
                        "longitude": 'N/A',
                        "country_calling_code": 'N/A',
                        "org": 'N/A'
                    }
                    return render(request, 'search_result.html', context=context)
            elif is_ip_address(search_detial):
                try:
                    #request api from https://ipapi.co
                    response = requests.get(f"https://ipapi.co/{search_detial}/json/")
                    data = response.json()

                    # Get the host name and IP address of the local machine
                    local_host_name = socket.gethostname()

                    rg = data['region']
                    # print("here") 
                    country = data['country_name']
                    country_code = data["country_code"]
                    city = data["city"]
                    latitude = data["latitude"]
                    longitude = data["longitude"]
                    country_calling_code = data["country_calling_code"]
                    org = data["org"]

                    context = {
                            "search_detial": search_detial,
                            "ip_address":ip_address,
                            "local_host":local_host_name,
                            "region": rg,
                            "country": country,
                            "country_code": country_code,
                            "city": city,
                            "latitude": latitude,
                            "longitude": longitude,
                            "country_calling_code": country_calling_code,
                            "org": org
                            }
                    return render(request, 'search_result.html', context=context)
                except:
                    # messages.warning(request, "Please, correct your IP Address!")
                    print("ip")
                    context = {
                        "search_detial": search_detial,
                        "ip_address":"N/A",
                        "local_host": "N/A",
                        "region": 'N/A',
                        "country": 'N/A',
                        "country_code": 'N/A',
                        "city": 'N/A',
                        "latitude": 'N/A',
                        "longitude": 'N/A',
                        "country_calling_code": 'N/A',
                        "org": 'N/A'
                    }
                    return render(request, 'search_result.html', context=context)
            else:
                print("else")
                context = {
                    "search_detial": search_detial,
                    "ip_address":"N/A",
                    "local_host": "N/A",
                    "region": 'N/A',
                    "country": 'N/A',
                    "country_code": 'N/A',
                    "city": 'N/A',
                    "latitude": 'N/A',
                    "longitude": 'N/A',
                    "country_calling_code": 'N/A',
                    "org": 'N/A'
                }
                return render(request, 'search_result.html', context=context)   
        else: 
            return render(request, 'index.html')
    else:
        print("method not mecth")
