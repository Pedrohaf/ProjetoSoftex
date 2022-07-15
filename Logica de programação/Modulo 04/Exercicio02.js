class MinhaConta{
    static cont = 0
    constructor(agencia, saldo, numero){
        this.agencia = agencia;
        this.saldo = saldo;
        this.numero = numero;
    }
    
    get saldo(){
        return this._saldo;
    }

    set saldo(valor){
        this._saldo = valor;
    }
    
    sacar(valor){
        if(valor>this._saldo){
            return 'Operação invalida'
        }
        cont++
        this._saldo = this._saldo - valor
        return this._saldo
    
    }

    depositar(valor){
        cont++
        this._saldo = this._saldo + valor
        return this._saldo
    
    }
}

depositar(100)

console.log("você ja sacou ou depositou na sua conta hoje: " + cont + " vezes")



