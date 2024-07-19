# from typing import List, Union
# from pydantic import BaseModel
# from datetime import datetime
# from decimal import Decimal

# class PersonalMedicoBase(BaseModel):
 

#     Departamento_ID: int
#     Cedula_Profesional: str
#     Tipo: str
#     Especialidad: str
#     Fecha_Registro: datetime
#     Fecha_Contratacion: datetime
#     Fecha_Termino_Contrato: datetime
#     Salario: Decimal
#     Estatus: str
#     Fecha_Actualizacion: datetime

# class PersonalMedicoCreate(PersonalMedicoBase):
#     pass

# class PersonalMedicoUpdate(PersonalMedicoBase):
#     pass

# class PersonalMedico(PersonalMedicoBase):
#     id: int
#     #owner_id: int clave foranea
#     class Config:
#         orm_mode = True