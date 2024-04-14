from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import subprocess
import os

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

def server_status():
    # Check if the server process is running
    result = os.popen('screen -ls').read()
    if '.minecraft'  in result:
        print("Server is running.")
        return True
    else:
        print("Server is not running.")
        return False
    #pid_check = os.system("pgrep -f 'minecraft_server.jar' >/dev/null")
    #return pid_check == 0

def server_command(command):
    # Send a command to the server using screen
    os.system(f"screen -S minecraft -p 0 -X stuff '{command}\r'")

def start_minecraft_server(request):
    try:
        if not server_status():
            os.chdir("/root/1.0.980TekxitPiServer/")
            os.system('screen -dmS "minecraft" java -Xmx4G -Xms4G -jar forge-1.12.2-14.23.5.2860.jar nogui')
            return render(request, 'main_page.html', {'message': 'Minecraft server started successfully.'})
        else:
            return render(request, 'main_page.html', {'message': 'server is already running .'})
    except Exception as e:
        # Handle any errors that occur during command execution
        return render(request, 'main_page.html', {'error': str(e)})

def stop_minecraft_server(request):
    try:
        if server_status():
            server_command('stop')
            return render(request, 'main_page.html', {'message': 'Minecraft server stopped successfully.'})
        else:
            return render(request, 'main_page.html', {'message': 'server not running.'})
    except Exception as e:
        # Handle any errors that occur during command execution
        return render(request, 'main_page.html', {'error': str(e)})
