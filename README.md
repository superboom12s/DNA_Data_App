# DNA Data App
## Ver. 1.2.0

> [!IMPORTANT]
> ### This proyect is in spanish :es: for now but it will be translated to english soon.

Esta aplicación trata de una _**libreria** con diferentes herramientas para manipular los datos de un código de **ADN** o **ARN**_ y sus respectivas proteinas, puede pasar de un código a otro, mostrar las proteinas que contiene un código... estas son las funciones de la libreria:


  - `trans(Codigo)` [^1]  
  - `dividirEnTres(Codigo)` [^2]
  - `encontrarProt(Codigo)` [^3]
  - `proteinList(Codigo)` [^4]
  - `tipo(Codigo, tipo[opcional])` [^5]
  - `encontrarCodigo(Proteina)` [^6]
  - `codigoList(Proteinas, tipo[opcional])` [^7]
  - `Datos(Codigo)` [^8]



> [!NOTE]
> La libreria esta hecha para aceptar tanto _ADN_ como _ARNm_ de entrada en las funciones que lo requieran, pero **la salida puede no ser la misma que la del valor introducido**, preste atención a la documentación en caso necesarío.

> [!TIP]
> Puedes encontrar la documentación mostrada anteriormente usando `ayuda()` o `help()`.
‎ ‎ ‎ ‎
[^1]: `trans(Codigo)` -> Si el valor introducido es _ADN_ lo transforma a _ARN_ y viceversa.
[^2]: `dividirEnTres(Codigo)` -> Divide en bloques un codigo de _ADN_ o _ARN_. Devuelve una lista.
[^3]: `encontrarProt(Codigo)` -> Encuentra **UNA** proteina de un bloque de codigo (se convierte a _ARN_ de forma automatica).
[^4]: `proteinList(Codigo)` -> Transforma una tira de _ADN_ (o varios _ARN_ en una sola tira) en **todas** las proteinas que contiene esa informacion.
[^5]: `tipo(Codigo, tipo[opcional])` -> Comprueba si el valor introducido es _ADN_ o _ARN_. _En caso de tener una segunda entrada_ traduce el codigo en un tipo especifico indicado por la segunda entrada. Si no se puede determinar el tipo, devolvera _ADN_ por defecto.
[^6]: `encontrarCodigo(Proteina)` -> **Indica el/los codigo(s)** necesario(s) para obtener una proteina especifica.
[^7]: `codigoList(Proteinas, tipo[opcional])` -> Hace una lista del _ADN_ necesario para obtener unas proteinas especificas. El tipo (opcional), por defecto es _ADN_, aunque se puede seleccionar _ARN_. En caso de ser ARN, el resultado viene separado por espacios.
[^8]: `Datos(Codigo)` -> Indica **todos los datos** de el codigo en la **terminal**.


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/superboom12s/DNA_Data_App/assets/85897199/9b7fa662-d65e-42c5-813d-cf9c339a7c69">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/superboom12s/DNA_Data_App/assets/85897199/b8da79ae-efcc-4274-99a8-f1fccb57647a">
  <img alt="Foto de Michiru Kagemori (y/o Nazuna Hiwatashi) dependiendo de si usa modo oscuro o modo claro." src="https://github.com/superboom12s/DNA_Data_App/assets/85897199/0c1cc0c2-3d0c-44f0-bf3c-f59c002fcfd7">
</picture>

> I **do not** own any of the 3 posible images that can be shown here.
