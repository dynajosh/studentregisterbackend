import json

def test_create_student(client):
    data = {
        "firstname" : "Badman",
        "lastname" : "Josh",
        "teacher_id" : 1,
        "is_active" : True
    }
    response = client.post("/students/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["lastname"] == "Josh"


