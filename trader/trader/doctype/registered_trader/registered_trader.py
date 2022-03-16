# Copyright (c) 2021, Hemant Pema and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import json
import uuid

class RegisteredTrader(Document):
	pass

@frappe.whitelist(allow_guest=False)
def generate_key():
	return uuid.uuid4()

@frappe.whitelist(allow_guest=True)
def ports(license, broker, account, push, pull, pub):
	exists = frappe.db.exists('Registered Trader',{'license_key': license})
	filters = [
		["Broker Account", "broker", "=", broker],
		["Broker Account", "parent", "=", exists],
		["Broker Account", "account_number", "=", account]
	]
	fields = ["push", "pull", "pub"]

	brokeraccount = frappe.get_all("Broker Account", filters=filters, fields=fields) or {}
	return brokeraccount

@frappe.whitelist(allow_guest=True)
def set_ports(license, registered_trader):
	exists = frappe.db.exists('Registered Trader',{'license_key': license})
	accounts = []
	#frappe.logger().info("exists: " + str(exists))
	#frappe.logger().info(registered_trader.get("broker_accounts")[0].get("push"))
	if exists:
		#trader = frappe.get_doc("Registerd Trader", exists)
		for broker in registered_trader.get("broker_accounts"):
			#frappe.logger().info("------ broker: " + str(broker))
			#frappe.logger().info("------ broker.port: " + str(broker.get("pull")))
			#frappe.logger().info("------ broker.port: " + str(broker.get("push")))
			#frappe.logger().info("------ broker.port: " + str(broker.get("pub")))
			
			# frappe.logger().info(broker.get('push'))
			filters = [
				["Broker Account", "broker", "=", broker.get('broker')],
				["Broker Account", "parent", "=", exists],
				["Broker Account", "account_number", "=", broker.get('account_number')]
			]
			#fields = ["push", "pull", "pub"]

			found = frappe.get_all("Broker Account", filters=filters) or None
			#frappe.logger().info("------ found: " + str(found))
			if found:
				brokeraccount = frappe.get_doc("Broker Account", found[0].get("name"))
				brokeraccount.push = broker.get('push')
				brokeraccount.pull = broker.get('pull')
				brokeraccount.pub = broker.get('pub')
				brokeraccount.save()
				accounts.append(brokeraccount)
			else:
				doc = frappe.get_doc({
					"doctype": "Broker Account",
					"push": broker.get('push'),
					"pull": broker.get('pull'),
					"pub": broker.get('pub'),
					"parent": exists,
					"broker": broker.get('broker'),
					"account_number": broker.get('account_number'),
					"parentfield": "broker_accounts",
					"parenttype": broker.get("parenttype")
					})
				doc.insert()
				accounts.append(doc)

	return accounts

@frappe.whitelist(allow_guest=True)
def check_registered(license, hdd_serial):
	bFound = False

	exists = frappe.db.exists('Registered Trader',{'license_key': license})
	if exists:
		registered = frappe.get_doc('Registered Trader', exists)
		for hdd in registered.attached_machines:
			if hdd.hard_drive_serial_number == hdd_serial:
				bFound = True
				break
		if bFound == False:
			#Add the serial number on the license
			bFound = True
	else:
		#Looking for hdd serial incase its entire folder is copied
		exists =
	return bFound

@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

