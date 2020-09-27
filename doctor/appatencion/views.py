from django.shortcuts import render
from django.views.generic.base import TemplateView


class InicioView(TemplateView):
    template_name = "index.html"

class InicioLoginView(TemplateView):
    template_name = "inicio-login/login.html"

class RegistroLoginView(TemplateView):
    template_name = "inicio-login/registrar.html"

class PacienteView(TemplateView):
    template_name = "paciente/paciente.html"

class PacienteRegistroView(TemplateView):
    template_name = "paciente/registro.html"

class DoctorView(TemplateView):
    template_name = "doctor/doctor.html"

class HistoriaView(TemplateView):
    template_name = "historial/historia-clinica.html"

class CitaView(TemplateView):
    template_name = "atencion/cita.html"

class AgendaView(TemplateView):
    template_name = "agenda/agenda-consulta.html"

class HorarioView(TemplateView):
    template_name = "configuracion/horario.html"

class RecetaView(TemplateView):
    template_name = "configuracion/receta.html"

class AntecedentesView(TemplateView):
    template_name = "configuracion/antecedentes.html"

class UsuarioView(TemplateView):
    template_name = "inicio-login/usuario.html"