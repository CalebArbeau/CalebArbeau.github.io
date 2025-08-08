import dearpygui.dearpygui as dpg
import os
import subprocess
import debloater
import syncro
import my_helper

# -------------------------------------- DPG Callbacks -------------------------------------
 
def sendPowershell(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    print("Powershell is now running command: " + cmd + "\n\n")

    print("Powershell output:\n" + str(completed))
    return completed

def debloat():
    sendPowershell("Set-ExecutionPolicy RemoteSigned")
    sendPowershell(
        r"Set-Location 'programs\Win11Debloat-master' ; .\Win11Debloat.ps1 -Silent -DisableWidgets -HideChat -HideTaskview -HideSearchTb -DisableRecall -DisableCopilot -DisableBing -RemoveW11Outlook"
    )

def setSyncroURL():
    url = dpg.get_value(syncroUrl)
    dpg.set_item_user_data(syncroDownloadBtn, url)

# ---------------------------------------- DPG Tabs ----------------------------------------

dpg.create_context()

with dpg.window(label="NetDNA Quick Copy Files", tag="Primary Window"):
    with dpg.tab_bar(label="Tab Bar"):
        with dpg.tab(label="Debloat"):
                raphireDownloadBtn = dpg.add_button(
                    label="Download Raphire", callback=debloater.qdebloat
                )
                delete = dpg.add_button(
                    label="Delete Raphire", callback=debloater.remove_debloater
                )
                debloat_windows = dpg.add_button(label="Debloat Windows", callback=debloat)
        with dpg.tab(label="SyncroMSP"):
            syncroUrl = dpg.add_input_text(label="Download URL", default_value="https://l.netnda.io/", callback=setSyncroURL)
            syncroDownloadBtn = dpg.add_button(enabled=True, label="Download Syncro", callback=syncro.download)

# --------------------------------------- DPG Config ---------------------------------------

dpg.create_viewport(
    title="Fast Windows Setup",
    width=650,
    height=300,
    small_icon=my_helper.getCurPath() + 'FWS.ico',
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()