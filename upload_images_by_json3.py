from dataclasses import dataclass
import json
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings
from catalog_app.models import Good


@dataclass
class Response:
    ok: bool = False


def get(link: str) -> requests.Response:
    try:
        return requests.get(link, timeout=10)
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.Timeout,
    ):
        return Response()


def save_image(good: Good, attr_name: str, link: str) -> None:
    result = get(link)
    if result.ok:
        img_temp = NamedTemporaryFile()
        img_temp.write(result.content)
        img_temp.flush()
        good.image1.save("image.jpg", File(img_temp), save=True)


def run_upload() -> None:
    with open(
        settings.BASE_DIR / "links3.json", mode="+r", encoding="utf-8-sig"
    ) as file:
        data = json.load(file)
        count = len(data.get("data"))
        for _, item in enumerate(data.get("data")):
            print(f"{_}/{count}")
            art = item.get("art")
            good = Good.objects.filter(art=art).first()
            if good:
                link1 = item.get("link1")
                if link1 and not good.image1:
                    result = get(link1)
                    if result.ok:
                        img_temp = NamedTemporaryFile()
                        img_temp.write(result.content)
                        img_temp.flush()
                        good.image1.save("image.jpg", File(img_temp), save=True)

                good.save()
