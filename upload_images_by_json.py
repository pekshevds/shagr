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
        return requests.get(link)
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
        return Response()


def save_image(good: Good, attr_name: str, link: str) -> None:
    result = get(link)
    if result.ok:
        img_temp = NamedTemporaryFile()
        img_temp.write(result.content)
        img_temp.flush()
        match attr_name:
            case "link1":
                good.image1.save("image.jpg", File(img_temp), save=True)
            case "link2":
                good.image2.save("image.jpg", File(img_temp), save=True)
            case "link3":
                good.image3.save("image.jpg", File(img_temp), save=True)


def run_upload() -> None:
    with open(
        settings.BASE_DIR / "links.json", mode="+r", encoding="utf-8-sig"
    ) as file:
        data = json.load(file)
        count = len(data.get("data"))
        for _, item in enumerate(data.get("data")):
            print(f"{_}/{count}")
            good_id = item.get("id")
            good = Good.objects.filter(id=good_id).first()
            if good:
                link1 = item.get("link1")
                if link1 and good.image1 is None:
                    result = get(link1)
                    if result.ok:
                        img_temp = NamedTemporaryFile()
                        img_temp.write(result.content)
                        img_temp.flush()
                        good.image1.save("image.jpg", File(img_temp), save=True)

                link2 = item.get("link2")
                if link2 and good.image2 is None:
                    result = get(link2)
                    if result.ok:
                        img_temp = NamedTemporaryFile()
                        img_temp.write(result.content)
                        img_temp.flush()
                        good.image2.save("image.jpg", File(img_temp), save=True)

                link3 = item.get("link3")
                if link3 and good.image3 is None:
                    result = get(link3)
                    if result.ok:
                        img_temp = NamedTemporaryFile()
                        img_temp.write(result.content)
                        img_temp.flush()
                        good.image3.save("image.jpg", File(img_temp), save=True)
                good.save()
