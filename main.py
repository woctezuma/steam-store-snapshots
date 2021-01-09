import json


def load_data(api_interface_name):
    fname = "data/{}.json".format(api_interface_name)

    with open(fname, "r", encoding="utf8") as f:
        data = json.load(f)

    if api_interface_name == "ISteamApps":
        app_list = data["applist"]["apps"]
    else:
        app_list = data["response"]["apps"]

    num_apps = len(app_list)

    print("[{}] #apps = {}".format(api_interface_name, num_apps))

    return app_list


if __name__ == "__main__":
    app_list_ISA = load_data(api_interface_name="ISteamApps")
    app_list_ISS = load_data(api_interface_name="IStoreService")
