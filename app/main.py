from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.db_helper import templates_collection
from app.helpers import detect_type

app = FastAPI()


@app.post("/get_form")
async def get_form(request: Request):
    form_data = await request.form()
    form_data_dict = dict(form_data)

    detected = {k: detect_type(v) for k, v in form_data_dict.items()}

    all_templates = list(templates_collection.find({}))

    for tpl in all_templates:
        template_name = tpl.get("name")
        tpl_fields = {k: v for k, v in tpl.items() if k != "_id" and k != "name"}

        match = True
        for field_name, field_type in tpl_fields.items():
            if field_name not in detected or detected[field_name] != field_type:
                match = False
                break

        if match:
            return JSONResponse(content={"template_name": template_name})

    return JSONResponse(content=detected)
