import json

def test_create_student(client):
    data = {
        "firstname" : "Badman",
        "lastname" : "Josh",
        "teacher_id" : 1,
        "is_active" : True
    }
    response = client.post("/students/create-student", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["lastname"] == "Josh"



def test_get_all_students(client):
    data = {
        "firstname" : "Badman",
        "lastname" : "Josh",
        "teacher_id" : 1,
        "is_active" : True
    }
    client.post("/students/create-student/", json.dumps(data))
    client.post("/students/get-student/", json.dumps(data))

    response = client.get("/stduents/get-all-students/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


