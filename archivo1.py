class Veterinario:
    def __init__(self, nombre = None, especialidad = None):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def iniciar_sesion(self):
        print('Veterinario está iniciando sesión...')

veterinario1 = Veterinario()
veterinario1.iniciar_sesion()
veterinario1.nombre = 'Juan Pablo'
veterinario1.especialidad = 'Caninos y especies menores'
print(veterinario1.nombre)
print(veterinario1.especialidad)

veterinario1.especialidad = 'Vacunos'

print(veterinario1.especialidad)

