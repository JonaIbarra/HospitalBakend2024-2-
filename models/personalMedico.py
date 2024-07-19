# from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date, DECIMAL
# from sqlalchemy.orm import relationship
# from config.db import Base
# import enum, datetime



# class TipoEnum(enum.Enum):
#     Médico = "Médico"
#     Enfermero = "Enfermero"
#     Administrativo = "Administrativo"
#     Directivo = "Directivo"
#     Apoyo = "Apoyo"
#     Residente = "Residente"
#     Interno = "Interno"


# class Persona(Base):
#     __tablename__ = "tbb_personal_medico"

#     Persona_ID = Column(Integer, primary_key=True)
#     Departamento_ID = Column(Integer)
#     Cedula_Profesional = Column(String(100))
#     Tipo = Column(Enum(TipoEnum)),
#     Especialidad = Column(String(255))
#     Fecha_Registro = Column(DateTime, default=datetime.now())
#     Fecha_Contratacion = Column(DateTime)
#     Fecha_Termino_Contrato = Column(DateTime)
#     Salario = Column(DECIMAL(10, 2))
#     Estatus = Column(Enum("Activo", "Inactivo"))
#     Fecha_Actualizacion = Column(DateTime)

