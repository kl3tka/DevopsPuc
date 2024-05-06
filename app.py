from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    valor = request.args.get("valor", "")
    valor2 = request.args.get("valor2", "")
    if valor and valor2:
        resultado = operacao(valor, valor2)
    else:
        resultado = ""

    return (
            """<h2> Divisor.</h2>"""
            """<br>"""
            """<form action="" method="get">
                    <input type="text" name="valor">
                    <input type="text" name="valor2">
                    <input type="submit" value="Resultado">
                </form>"""
            + "Ultimo Valor digitado: " + valor + valor2 + '</br>' +
            "Dobro: " + '<a id="resultado">' + resultado + '</a>'

    )


@app.route("/<int:valor>")
def operacao(valor, valor2):
    """Efetuado a metade do numero"""
    resultado = float(valor) / float(valor2)
    return str(resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(host="0.0.0.0", port=8080, debug=False)
