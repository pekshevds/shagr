import json
from httpx import Client
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings
from catalog_app.models import Good


def save_image(good: Good, attr_name: str, link: str) -> None:
    result = Client().get(link)
    if 200 <= result.status_code < 400:
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
        settings.BASE_DIR / "links_test.json", mode="+r", encoding="utf-8-sig"
    ) as file:
        data = json.load(file)
        for item in data.get("data"):
            good_id = item.get("id")
            good = Good.objects.filter(id=good_id).first()
            if good:
                link1 = item.get("link1")
                if link1:
                    result = Client().get(link1)
                    if 200 <= result.status_code < 400:
                        img_temp = NamedTemporaryFile()
                        img_temp.write(result.content)
                        img_temp.flush()
                        good.image1.save("image.jpg", File(img_temp), save=True)

                link2 = item.get("link2")
                if link2:
                    result = Client().get(link2)
                    if 200 <= result.status_code < 400:
                        img_temp = NamedTemporaryFile()
                        img_temp.write(result.content)
                        img_temp.flush()
                        good.image2.save("image.jpg", File(img_temp), save=True)

                link3 = item.get("link3")
                if link3:
                    result = Client().get(link3)
                    if 200 <= result.status_code < 400:
                        img_temp = NamedTemporaryFile()
                        img_temp.write(result.content)
                        img_temp.flush()
                        good.image3.save("image.jpg", File(img_temp), save=True)
                good.save()
