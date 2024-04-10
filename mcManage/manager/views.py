from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import subprocess

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('manager:main_page')

    def get_success_url(self):
        return self.success_url

def logout_view(request):
    logout(request)
    return redirect('manager:main_page')
# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def start_minecraft_server(request):
    # Command to start Minecraft server (adjust path and command as needed)
    command = '/path/to/minecraft/server/start_script.sh'
    
    try:
        # Execute the command to start the Minecraft server
        subprocess.Popen(command, shell=True)
        # Optionally, you can redirect the user to another page after starting the server
        return render(request, 'main_page.html', {'message': 'Minecraft server started successfully.'})
    except Exception as e:
        # Handle any errors that occur during command execution
        return render(request, 'main_page.html', {'error': str(e)})
def stop_minecraft_server(request):
    # Command to stop Minecraft server (adjust path and command as needed)
    command = '/path/to/minecraft/server/stop_script.sh'
    
    try:
        # Execute the command to stop the Minecraft server
        subprocess.run(command, shell=True)
        # Optionally, you can redirect the user to another page after stopping the server
        return render(request, 'main_page.html', {'message': 'Minecraft server stopped successfully.'})
    except Exception as e:
        # Handle any errors that occur during command execution
        return render(request, 'main_page.html', {'error': str(e)})
