# Steam Store Snapshots

This repository contains data snapshots of the list of apps on the Steam store.

## Data

Data can provide from the following API interfaces:
-   `ISteamApps`
-   `IStoreService`

### `ISteamApps`

![Illustration for ISteamApps][illustration-ISteamApps]

A request is made to the following endpoint:

> `https://api.steampowered.com/ISteamApps/GetAppList/v2/?`

`ISteamApps` does not require any argument.

### `IStoreService`

![Illustration for IStoreService][illustration-IStoreService]

A request is made to the following endpoint:

> `https://api.steampowered.com/IStoreService/GetAppList/v1/?key=is_here_but_hidden&max_results=50000`

`IStoreService` should be called with the following arguments:
-   `key=is_here_but_hidden`: your access key,
-   `max_results=50000`: the number of apps to return at a time. Max is 50k.

Your access key is **secret**, and can be:
-   either your WebAPI key,
-   or your OAuth access token.

Please refer to the explanation below to figure out your secret key:

![Illustration for the secret key][illustration-secret-key]

## Unofficial API: GameDataCrunch

[GameDataCrunch][gdc-website] provides an unofficial API to retrieve the list of apps on the Steam store.

It can be an alternative if you don't have an access key for the official API.

A Python package [`gamedatacrunch`][gdc-github] is available on [PyPI][gdc-pypi].

## References

-   Official API:
    - [`ISteamApps` interface][steam-web-api-ISteamApps]
    - [`IStoreService` interface][steam-web-api-IStoreService]
    - [Steam Web API Documentation][steam-web-api-documentation]
-   Unofficial API:
    - Website: [GameDataCrunch][gdc-website]
    - Python package: [`gamedatacrunch`][gdc-github]@[PyPI][gdc-pypi]

[gdc-website]: <https://www.gamedatacrunch.com/>
[gdc-github]: <https://github.com/woctezuma/gamedatacrunch>
[gdc-pypi]: <https://pypi.org/project/gamedatacrunch/>

[steam-web-api-ISteamApps]: <https://steamapi.xpaw.me/#ISteamApps/GetAppList>
[steam-web-api-IStoreService]: <https://steamapi.xpaw.me/#IStoreService/GetAppList>
[steam-web-api-documentation]: <https://steamapi.xpaw.me/>

[illustration-ISteamApps]: <https://raw.githubusercontent.com/wiki/woctezuma/steam-store-snapshots/img/ISteamApps.png>
[illustration-IStoreService]: <https://raw.githubusercontent.com/wiki/woctezuma/steam-store-snapshots/img/IStoreService.png>
[illustration-secret-key]: <https://raw.githubusercontent.com/wiki/woctezuma/steam-store-snapshots/img/doc.png>
