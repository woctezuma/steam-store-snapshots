import json


def load_data(api_interface_name, page_no=1):
    if page_no == 1:
        file_suffix = ""
    else:
        file_suffix = f"_page_{page_no}"

    fname = f"data/{api_interface_name}{file_suffix}.json"

    with open(fname, "r", encoding="utf8") as f:
        data = json.load(f)

    if api_interface_name == "ISteamApps":
        app_list = data["applist"]["apps"]
    else:
        app_list = data["response"]["apps"]

    if (
        "response" in data
        and "have_more_results" in data["response"]
        and data["response"]["have_more_results"]
    ):
        app_list += load_data(api_interface_name, page_no + 1)

    num_apps = len(app_list)

    if page_no == 1:
        print(f"[{api_interface_name}] #apps = {num_apps}")

    return app_list


def save_app_ids(app_list):
    fname = "data/all_app_ids.txt"

    with open(fname, "w", encoding="utf8") as f:
        for app in app_list:
            app_id = app["appid"]
            f.write(f"{app_id}\n")

    return


if __name__ == "__main__":
    app_list_ISA = load_data(api_interface_name="ISteamApps")
    app_list_ISS = load_data(api_interface_name="IStoreService")
    save_app_ids(app_list_ISS)
