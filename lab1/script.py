import requests
from bs4 import BeautifulSoup

def get_omstu_faculties(url, filename="omstu_faculties.txt"):

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")


        faculty_elements = soup.find_all("a", href=lambda href: href and "http://www.omgtu.ru/general_information/faculties/" in href)

        faculties = []
        for element in faculty_elements:
            faculty_name = element.text.strip()
            faculties.append(faculty_name)


        with open(filename, "w", encoding="utf-8") as f:
            for faculty in faculties:
                f.write(faculty + "\n")

        print(f"Список факультетов успешно записан в файл: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    omstu_url = "https://omgtu.ru/general_information/faculties/"
    get_omstu_faculties(omstu_url)