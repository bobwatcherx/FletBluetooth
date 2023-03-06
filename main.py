from flet import *
import subprocess
import os

def main(page:Page):
	you_file = TextField(label="you file name")

	# AND DESTINATION MAC ADDRESS PHONE ANDROID
	# GET TEXTFIELD
	destination_mac = TextField(label="mac address")
	scan_result = Text(weight="bold")


	# NOW I SCAN DEVICES IS AVAILABLE
	def scan_devices():
		res = subprocess.check_output(["hcitool","scan"]).decode("utf-8")
		print(res)

		# AND SHOW RESULT DEVICES AVAILABEL IN FLET APP
		devices = [line.split('\t',maxsplit=1) for line in res.splitlines()[1:]]
		formated_devices = [
			f"mac address : {mac}\tdevices: {name}"
			for mac , name in devices
			]
		scan_result.value = "\n".join(formated_devices)
		page.update()

	# CALL FUNCTION WHEN FLET APP FIRST RUN
	# THEN SCAN AUTOMATICALY devices NEAR YOU
	scan_devices()



	def sendfilenow(e):
		# AND AFTER SUCCESS SCAN THEN SEND FILE
		# TO ANDROID WITH BLUETOOTH
		command = 'bluetooth-sendto --device=' + destination_mac.value + ' ' + you_file.value
		result = os.system(command)
		if result == 0 :
			print('SUccess Transfer guys !!!')
			page.snack_bar = SnackBar(
            Text("success sending !!",size=30),
            bgcolor="green"
                )
			page.snack_bar.open = True
			page.update()
		else :
			print('Failed send !!!')


	page.add(
	Column([
		Text("upload file to Bluetooth",size=25,
		weight="bold"
		),
		you_file,
		destination_mac,
		ElevatedButton("Send now guys",
			bgcolor="blue",color="white",
			on_click=sendfilenow
			),
		# AND SHOW RESULT OF SCAN DEVICES NEAR YOU
		scan_result
		])
	)


flet.app(target=main)
