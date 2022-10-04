import shutil, random, time, requests, platform, os



def generate():
        print("Generating Face...")
        r = requests.get("https://thispersondoesnotexist.com/image", stream=True)
        if r.status_code == 200:
            a = str(random.randint(0, 9999))
            with open(f"assets/faces/unsorted/{a}", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                print("Generated Face")
                if platform.system() == "Windows":
                    os.system(f"start assets/faces/unsorted/{a}")
                elif platform.system() == "Linux":
                    os.system(f"xdg-open assets/faces/unsorted/{a}")

            time.sleep(0.5)

