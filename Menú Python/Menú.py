import PrestamoDeFi # Importamos el módulo con las funciones y conexión a Ganache


def mostrar_menu():
    print("\nMenú de Interacción con el Contrato:")
    print("1. Dar de alta un prestamista")
    print("2. Dar de alta un cliente")
    print("3. Depositar garantía")
    print("4. Solicitar un préstamo")
    print("5. Aprobar un préstamo")
    print("6. Reembolsar un préstamo")
    print("7. Liquidar garantía")
    print("8. Obtener préstamos por prestatario")
    print("9. Obtener detalle de préstamo")
    print("0. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def main():
    while True:
        opcion = mostrar_menu()
        try:
            if opcion == '1':
                address = input("Introduce la dirección del nuevo prestamista: ")
                resultado = PrestamoDeFi.alta_prestamista(address)
                print(f"Resultado: {resultado}")
                
            elif opcion == '2':
                address = input("Introduce la dirección del nuevo cliente: ")
                prestamista_address = input("Introduce tu dirección de prestamista: ")  # Mejorar seguridad
                prestamista_private_key = input("Introduce tu clave privada de prestamista: ") # Mejorar seguridad
                resultado = PrestamoDeFi.alta_cliente(address, prestamista_address, prestamista_private_key)
                print(f"Resultado: {resultado}")
                
            elif opcion == '3':
                valor = input("Introduce el valor a depositar: ")
                direccion_cliente = input("Introduce la dirección del cliente: ")
                clave_privada_cliente = input("Introduce la clave privada del cliente: ") # Mejorar seguridad
                resultado = PrestamoDeFi.depositar_garantia(direccion_cliente, valor, clave_privada_cliente)
                print(f"Resultado: {resultado}")
                
            elif opcion == '4':
                monto = input("Introduce el monto del préstamo: ")
                plazo = input("Introduce el plazo del préstamo: ")
                direccion_cliente = input("Introduce tu dirección de cliente: ")
                clave_privada_cliente = input("Introduce tu clave privada de cliente: ") # Mejorar seguridad
                resultado = PrestamoDeFi.solicitar_prestamo(direccion_cliente, monto, plazo, clave_privada_cliente)
                print(f"Resultado: {resultado}")
                
            elif opcion == '5':
                address = input("Introduce la dirección del prestatario: ")
                prestamo_id = input("Introduce el ID del préstamo: ")
                prestamista_address = input("Introduce tu dirección de prestamista: ")
                prestamista_private_key = input("Introduce tu clave privada de prestamista: ") # Mejorar seguridad
                resultado = PrestamoDeFi.aprobar_prestamo(address,prestamo_id, prestamista_address, prestamista_private_key)
                print(f"Resultado: {resultado}")
                
            elif opcion == '6':
                prestamo_id = input("Introduce el ID del préstamo a reembolsar: ")
                cliente_address = input("Introduce tu dirección de cliente: ")
                cliente_private_key = input("Introduce tu clave privada de cliente: ") # Mejorar seguridad
                resultado = PrestamoDeFi.reembolsar_prestamo(prestamo_id, cliente_address,cliente_private_key)
                print(f"Resultado: {resultado}")
                
            elif opcion == '7':
                address = input("Introduce la dirección del prestatario: ")
                prestamo_id = input("Introduce el ID del préstamo: ")
                resultado = PrestamoDeFi.liquidar_garantia(address, prestamo_id)
                print(f"Resultado: {resultado}")
                
            elif opcion == '8':
                address = input("Introduce la dirección del prestatario: ")
                resultado = PrestamoDeFi.obtener_prestamos_por_prestatario(address)
                print(f"Préstamos: {resultado}")
                
            elif opcion == '9':
                 address = input("Introduce la dirección del prestatario: ")
                 prestamo_id = input("Introduce el ID del préstamo: ")
                 resultado = PrestamoDeFi.obtener_detalle_de_prestamo(address, prestamo_id)
                 print(f"Detalle del préstamo: {resultado}")
                 
            elif opcion == '0':
                break
            
            else:
                print("Opción no válida, por favor intenta de nuevo.")
                
        except Exception as e:
                print(f"Ocurrió un error: {e}")
                if __name__ == "__main__":
                    main()
                



from web3 import Web3
from web3.exceptions import Web3Exception

# Intentar conectarse a la red de Ganache

try:
    ganache_url = "http://localhost:7545"
    w3 = Web3(Web3.HTTPProvider(ganache_url))

if not w3.is_connected():
    print("No se pudo conectar a Ganache. Asegúrate de que Ganache esté en funcionamiento.")

exit()

except Exception as e:
print(f"Error al intentar conectar con Ganache: {e}")
exit()
print("Conectado a Ganache")

# Direccion del contrato inteligente desplegado 
contract_address = "0x7AF151bC31E932e6b0a8548Bc89f6ea330a81F59" # Cambia por la dirección del contrato
# Direccion del socio principal
socio_principal_address = "0x92Cdd340BCE528C8856565F74fdEdBAc36cE78e8" # Cambia por la dirección del socio principal
# Clave privada del socio principal (necesaria para firmartransacciones)
socio_principal_private_key = "0x9f143dd7f7286f0ae0af80e693cdeac39965e8b0804d3a2e543b4f609f9ba973" # Cambia por la clave privada del socio principal

contract_abi =[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "prestatario",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "monto",
				"type": "uint256"
			}
		],
		"name": "GarantiaLiquidada",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "prestatario",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "monto",
				"type": "uint256"
			}
		],
		"name": "PrestamoAprobado",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "prestatario",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "monto",
				"type": "uint256"
			}
		],
		"name": "PrestamoReembolsado",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "prestatario",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "monto",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "plazo",
				"type": "uint256"
			}
		],
		"name": "SolicitudPrestamo",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "nuevoCliente",
				"type": "address"
			}
		],
		"name": "altaCliente",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "nuevoPrestamista",
				"type": "address"
			}
		],
		"name": "altaPrestamista",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "prestatario_",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "id_",
				"type": "uint256"
			}
		],
		"name": "aprobarPrestamo",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "clientes",
		"outputs": [
			{
				"internalType": "bool",
				"name": "activado",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "saldoGarantia",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "depositarGarantia",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "empleadosPrestamista",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "prestatario_",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "id_",
				"type": "uint256"
			}
		],
		"name": "liquidarGarantia",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "prestatario_",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "id_",
				"type": "uint256"
			}
		],
		"name": "obtenerDetallesPrestamo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "prestatario",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "monto",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "plazo",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "tiempoSolicitud",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "tiempoLimite",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "aprobado",
						"type": "bool"
					},
					{
						"internalType": "bool",
						"name": "reembolsado",
						"type": "bool"
					},
					{
						"internalType": "bool",
						"name": "liquidado",
						"type": "bool"
					}
				],
				"internalType": "struct PrestamoDeFi.Prestamo",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "prestatario_",
				"type": "address"
			}
		],
		"name": "obtenerPrestamosPorPrestatario",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id_",
				"type": "uint256"
			}
		],
		"name": "reembolsarPrestamo",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "socioPrincipal",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "monto_",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "plazo_",
				"type": "uint256"
			}
		],
		"name": "solicitarPrestamo",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]


contract = w3.eth.contract(address=contract_address, abi=contract_abi)

#Función para enviar transaccion:

def enviar_transaccion(w3, txn_dict, private_key):
    try:
signed_txn = w3.eth.account.sign_transaction(txn_dict,private_key=private_key)


txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
return txn_receipt
except Exception as e:
# Lanzar la excepción para ser capturada por la función que llama
raise Exception(f"Error al enviar la transacción: {e}")



def dar_alta_prestamista(nuevo_prestamista_address):
      # Verificar si el prestamista ya existe en el contrato
    if contrato.functions.esPrestamista(nuevo_prestamista_address).call():
        return "El prestamista ya está registrado en el contrato."
    
    # Construir la transacción para agregar el nuevo prestamista
    transaccion = contrato.functions.agregarPrestamista(nuevo_prestamista_address)
    gas = transaccion.estimateGas({'from': socio_principal_address.address})
    nonce = web3.eth.getTransactionCount(socio_principal_address.address)
    transaccion_dict = transaccion.buildTransaction({
        'gas': gas,
        'gasPrice': web3.toWei('10', 'gwei'),
        'nonce': nonce,
        'from': socio_principal_address,
    })
    
    # Firmar la transacción
    transaccion_firmada = socio_principal_address.signTransaction(transaccion_dict)
    
    # Enviar la transacción a la blockchain
    web3.middleware_onion.add(construct_sign_and_send_raw_middleware(socio_principal_address.privateKey))
    tx_hash = web3.eth.sendRawTransaction(transaccion_firmada.rawTransaction)
    
    # Esperar la confirmación de la transacción
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    
    # Verificar si la transacción fue exitosa
    if tx_receipt.status == 1:
        return "El prestamista fue agregado exitosamente al contrato."
    else:
        return "Hubo un problema en la transacción. El prestamista no pudo ser agregado al contrato."
    


def alta_cliente( nuevo_cliente_address, prestamista_address, prestamista_private_key):
    # Verificar si el cliente ya está registrado en el contrato
    if contrato.functions.esCliente(nuevo_cliente_address).call():
        return "El cliente ya está registrado en el sistema."
    
    # Construir la transacción para registrar al nuevo cliente
    transaccion = contrato.functions.registrarCliente(nuevo_cliente_address)
    gas = transaccion.estimateGas({'from': prestamista_address})
    nonce = web3.eth.getTransactionCount(prestamista_address)
    transaccion_dict = transaccion.buildTransaction({
        'gas': gas,
        'gasPrice': web3.toWei('10', 'gwei'),
        'nonce': nonce,
        'from': prestamista_address,
    })
    
    # Firmar la transacción con la clave privada del prestamista
    cuenta_prestamista = Account.from_key(prestamista_private_key)
    transaccion_firmada = cuenta_prestamista.signTransaction(transaccion_dict)
    
    # Enviar la transacción a la blockchain
    web3.middleware_onion.add(construct_sign_and_send_raw_middleware(prestamista_private_key))
    tx_hash = web3.eth.sendRawTransaction(transaccion_firmada.rawTransaction)
    
    # Esperar la confirmación de la transacción
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    
    # Verificar si la transacción fue exitosa
    if tx_receipt.status == 1:
        return "El cliente ha sido registrado con éxito."
    else:
        return "Hubo un problema en la transacción. El cliente no pudo ser registrado."


def alta_cliente(nuevo_cliente_address, prestamista_address, prestamista_private_key):
    # Conexión a la red Ethereum (ajusta la URL según tu red)
    w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
   

    # Verificar si el cliente ya está registrado
    try:
        registrado = contrato.functions.esClienteRegistrado(nuevo_cliente_address).call()
        if registrado:
            return "Error: El cliente ya está registrado."
    except Exception as e:
        return f"Error al verificar el registro del cliente: {str(e)}"

    # Transacción para registrar al nuevo cliente
    try:
        nonce = w3.eth.getTransactionCount(prestamista_address)
        tx = contrato.functions.registrarCliente(nuevo_cliente_address).buildTransaction({
            'chainId': w3.eth.chainId,
            'gas': 1000000,
            'gasPrice': w3.toWei('10', 'gwei'),
            'nonce': nonce,
        })
        
        firmado_tx = w3.eth.account.signTransaction(tx, private_key=prestamista_private_key)
        tx_hash = w3.eth.sendRawTransaction(firmado_tx.rawTransaction)
        w3.eth.waitForTransactionReceipt(tx_hash)
        return "El cliente ha sido registrado con éxito."
    except Exception as e:
        return f"Error al registrar al cliente: {str(e)}"


resultado = alta_cliente(nuevo_cliente_address, prestamista_address, prestamista_private_key)
print(resultado)

def depositar_garantia(direccion_cliente, valor, clave_privada_cliente):
    # Conexión a la red Ethereum (ajusta la URL según tu red)
    w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
    

    # Instancia del contrato
    contrato = w3.eth.contract(address=contrato_address, abi=contrato_abi)

    # Prepara la transacción con el monto de la garantía
    try:
        nonce = w3.eth.getTransactionCount(direccion_cliente)
        tx = contrato.functions.depositarGarantia().buildTransaction({
            'chainId': w3.eth.chainId,
            'gas': 1000000,  # Ajusta el límite de gas según sea necesario
            'gasPrice': w3.toWei('10', 'gwei'),  # Ajusta el precio del gas según sea necesario
            'value': w3.toWei(valor, 'ether'),  # Convertir el valor a wei
            'nonce': nonce,
        })
        firmado_tx = w3.eth.account.signTransaction(tx, private_key=clave_privada_cliente)
        tx_hash = w3.eth.sendRawTransaction(firmado_tx.rawTransaction)
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        if receipt.status == 1:
            return "La garantía ha sido depositada exitosamente."
        else:
            return "Error: La transacción ha fallado."
    except Exception as e:
        return f"Error al depositar la garantía: {str(e)}"


resultado = depositar_garantia(direccion_cliente, valor, clave_privada_cliente)
print(resultado)

def solicitar_prestamo(direccion_cliente, monto, plazo, clave_privada_cliente):
   
    # Verificar si el cliente tiene suficiente garantía (solo como ejemplo, deberías implementar la lógica real aquí)
    if monto * plazo > 1000000:
        tiene_suficiente_garantia = True
    else:
        tiene_suficiente_garantia = False
        
    return tiene_suficiente_garantia
    
    if not tiene_suficiente_garantia:
        return "Error: El cliente no tiene suficiente garantía para solicitar el préstamo."
    
    tiene_suficiente_garantia = verificar_garantia(monto, plazo)

# Llamada a la función
resultado = solicitar_prestamo(direccion_cliente, monto, plazo, clave_privada_cliente)



def aprobar_prestamo(prestatario_address, prestamo_id, prestamista_address, prestamista_private_key):
     # Verificar validez del préstamo y del prestatario (aquí puedes agregar tu lógica de validación)
    if not verificar_validez_prestamo(prestamo_id, prestatario_address):
        print("Error: El préstamo no es válido.")
        return

    # Verificar si el préstamo ya está aprobado (aquí puedes agregar tu lógica de verificación)
    if ya_aprobado(prestamo_id):
        print("Error: El préstamo ya está aprobado.")
        return

    # Construir la transacción
    transaccion = {
        'to': contrato_prestamos_address,  # Dirección del contrato de préstamos
        'from': prestamista_address,
        'gas': 2000000,  # Gas máximo permitido
        'gasPrice': web3.toWei('50', 'gwei'),  # Precio del gas
        'nonce': web3.eth.getTransactionCount(prestamista_address),
        'data': contrato_prestamos.functions.aprobarPrestamo(prestamo_id).buildTransaction()
    }

    # Firmar la transacción
    firma = web3.eth.account.signTransaction(transaccion, prestamista_private_key)

    try:
        # Enviar la transacción
        tx_hash = web3.eth.sendRawTransaction(firma.rawTransaction)
        # Esperar la confirmación de la transacción
        web3.eth.waitForTransactionReceipt(tx_hash)
        print("El préstamo ha sido aprobado exitosamente.")
    except Exception as e:
        print("Error al enviar la transacción:", e)
        
    aprobar_prestamo(prestatario_address, prestamo_id, prestamista_address, prestamista_private_key)

def reembolsar_prestamo(prestamo_id, cliente_address, cliente_private_key):
    # Conexión a la red Ethereum
    w3 = conectar_a_ethereum()

    # Cargar el contrato del préstamo (aquí se asume que hay un contrato en la red Ethereum)
    with open('contrato_prestamo_abi.json', 'r') as abi_file:
        abi = json.load(abi_file)
    
    contrato_address = '0x...direccion_del_contrato...'  # Dirección del contrato del préstamo
    contrato = w3.eth.contract(address=contrato_address, abi=abi)

    # Verificar si el préstamo es válido y si el cliente es el prestatario
    if contrato.functions.esValido(prestamo_id).call() and contrato.functions.prestatario(prestamo_id).call() == cliente_address:
        # Firma de la transacción
        cuenta = Account.from_key(cliente_private_key)

        # Crear la transacción
        transaccion = contrato.functions.reembolsarPrestamo(prestamo_id).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(cliente_address),
        })

        # Firmar la transacción
        transaccion_firmada = w3.eth.account.signTransaction(transaccion, private_key=cliente_private_key)

        # Enviar la transacción
        tx_hash = w3.eth.sendRawTransaction(transaccion_firmada.rawTransaction)

        # Esperar la confirmación
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        # Verificar el estado de la transacción
        if tx_receipt.status == 1:
            return "El préstamo ha sido reembolsado exitosamente."
        else:
            return "Error: La transacción ha fallado."
    else:
        return "Error: Préstamo inválido o cliente no autorizado."

# Uso de la función
resultado = reembolsar_prestamo("ID_DEL_PRESTAMO", "DIRECCION_ETHEREUM_DEL_CLIENTE", "CLAVE_PRIVADA_DEL_CLIENTE")
print(resultado)

# Función para liquidar la garantía de un préstamo
def liquidar_garantia(prestamo_id, prestamista_address, prestamista_private_key):
    # Conexión a la red Ethereum
    w3 = conectar_a_ethereum()

    # Cargar el contrato del préstamo (aquí se asume que hay un contrato en la red Ethereum)
    with open('contrato_prestamo_abi.json', 'r') as abi_file:
        abi = json.load(abi_file)
    
    contrato_address = '0x...direccion_del_contrato...'  # Dirección del contrato del préstamo
    contrato = w3.eth.contract(address=contrato_address, abi=abi)

    # Verificar si el préstamo está aprobado, no reembolsado y ha vencido el plazo
    if contrato.functions.aprobado(prestamo_id).call() and not contrato.functions.reembolsado(prestamo_id).call() and contrato.functions.vencido(prestamo_id).call():
        # Firma de la transacción
        cuenta = Account.from_key(prestamista_private_key)

        # Crear la transacción
        transaccion = contrato.functions.liquidarGarantia(prestamo_id).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(prestamista_address),
        })

        # Firmar la transacción
        transaccion_firmada = w3.eth.account.signTransaction(transaccion, private_key=prestamista_private_key)

        # Enviar la transacción
        tx_hash = w3.eth.sendRawTransaction(transaccion_firmada.rawTransaction)

        # Esperar la confirmación
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        # Verificar el estado de la transacción
        if tx_receipt.status == 1:
            return "La garantía ha sido liquidada exitosamente."
        else:
            return "Error: La transacción ha fallado."
    else:
        return "Error: El préstamo no cumple con los requisitos para liquidar la garantía."

# Uso de la función
resultado = liquidar_garantia("ID_DEL_PRESTAMO", "DIRECCION_ETHEREUM_DEL_PRESTAMISTA", "CLAVE_PRIVADA_DEL_PRESTAMISTA")
print(resultado)

def obtener_prestamos_por_prestatario(prestatario_address):
    # Conexión a la red Ethereum
    w3 = conectar_a_ethereum()

    # Cargar el contrato de préstamo (aquí se asume que hay un contrato en la red Ethereum)
    with open('contrato_prestamo_abi.json', 'r') as abi_file:
        abi = json.load(abi_file)
    
    contrato_address = '0x...direccion_del_contrato...'  # Dirección del contrato de préstamo
    contrato = w3.eth.contract(address=contrato_address, abi=abi)

    # Realizar la llamada al contrato para obtener la lista de IDs de préstamos del prestatario
    prestamos_ids = contrato.functions.obtenerPrestamosPorPrestatario(prestatario_address).call()

    return prestamos_ids

# Uso de la función
prestatario_address = "DIRECCION_ETHEREUM_DEL_PRESTATARIO"
lista_prestamos = obtener_prestamos_por_prestatario(prestatario_address)
print("IDs de préstamos asociados al prestatario:", lista_prestamos)

# Función para obtener detalles de un préstamo
def obtener_detalle_de_prestamo(prestatario_address, prestamo_id):
    # Conexión a la red Ethereum
    w3 = conectar_a_ethereum()

    # Cargar el contrato de préstamo (aquí se asume que hay un contrato en la red Ethereum)
    with open('contrato_prestamo_abi.json', 'r') as abi_file:
        abi = json.load(abi_file)
    
    contrato_address = '0x...direccion_del_contrato...'  # Dirección del contrato de préstamo
    contrato = w3.eth.contract(address=contrato_address, abi=abi)

    # Realizar la llamada al contrato para obtener los detalles del préstamo
    detalles_prestamo = contrato.functions.obtenerDetalleDePrestamo(prestatario_address, prestamo_id).call()

    return detalles_prestamo

# Uso de la función
prestatario_address = "DIRECCION_ETHEREUM_DEL_PRESTATARIO"
prestamo_id = "ID_DEL_PRESTAMO"
detalles_prestamo = obtener_detalle_de_prestamo(prestatario_address, prestamo_id)
print("Detalles del préstamo solicitado:", detalles_prestamo)



