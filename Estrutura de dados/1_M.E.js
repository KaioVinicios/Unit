class Paciente {
    constructor(nome, idade, condicao) {
        this.nome = nome;
        this.idade = idade;
        this.condicao = condicao;
        this.proximo = null;
        this.historicoConsultas = [];
    }

    adicionarConsulta(consulta) {
        this.historicoConsultas.push(consulta);
    }

    verHistorico() {
        if (this.historicoConsultas.length === 0) {
            console.log("Nenhuma consulta realizada.");
            return;
        }
        console.log(`Histórico de consultas para ${this.nome}:`);
        for (let i = this.historicoConsultas.length - 1; i >= 0; i--) {
            console.log(`- ${this.historicoConsultas[i]}`);
        }
    }
}


class RegistroPacientes {
    constructor() {
        this.head = null;
    }

    adicionarPaciente(paciente) {
        if (this.head === null) {
            this.head = paciente;
        } else {
            let atual = this.head;
            while (atual.proximo !== null) {
                atual = atual.proximo;
            }
            atual.proximo = paciente;
        }
        console.log(`${paciente.nome} foi adicionado ao registro de pacientes.`);
    }

    exibirPacientes() {
        if (this.head === null) {
            console.log("Nenhum paciente no registro.");
            return;
        }
        let atual = this.head;
        while (atual !== null) {
            console.log(`Paciente: ${atual.nome}, Idade: ${atual.idade}, Condição: ${atual.condicao}`);
            atual = atual.proximo;
        }
    }
}

class FilaAtendimentoPrioritario {
    constructor() {
        this.fila = [];
    }

    adicionarPaciente(paciente) {
        this.fila.push(paciente);
        console.log(`${paciente.nome} foi adicionado à fila de atendimento prioritário.`);
    }

    atenderProximoPaciente() {
        if (this.fila.length === 0) {
            console.log("Nenhum paciente na fila de prioridade.");
            return;
        }

        let pacienteGrave = this.fila.reduce((maisGrave, pacienteAtual) => 
            pacienteAtual.condicao > maisGrave.condicao ? pacienteAtual : maisGrave
        );

        this.fila = this.fila.filter(p => p !== pacienteGrave);
        console.log(`${pacienteGrave.nome} está sendo atendido.`);
    }

    exibirFila() {
        if (this.fila.length === 0) {
            console.log("A fila de atendimento prioritário está vazia.");
            return;
        }
        console.log("Fila de atendimento prioritário:");
        this.fila.forEach(paciente => {
            console.log(`Paciente: ${paciente.nome}, Condição: ${paciente.condicao}`);
        });
    }
}

let registroPacientes = new RegistroPacientes();
let filaPrioritaria = new FilaAtendimentoPrioritario();

let paciente1 = new Paciente("João", 45, 3);
let paciente2 = new Paciente("Maria", 60, 5);
let paciente3 = new Paciente("Carlos", 25, 2);

registroPacientes.adicionarPaciente(paciente1);
registroPacientes.adicionarPaciente(paciente2);
registroPacientes.adicionarPaciente(paciente3);

registroPacientes.exibirPacientes();

filaPrioritaria.adicionarPaciente(paciente1);
filaPrioritaria.adicionarPaciente(paciente2);
filaPrioritaria.adicionarPaciente(paciente3);

filaPrioritaria.exibirFila();

filaPrioritaria.atenderProximoPaciente();

filaPrioritaria.exibirFila();

paciente1.adicionarConsulta("Consulta de rotina - 01/09/2024");
paciente1.adicionarConsulta("Exame de sangue - 05/09/2024");

paciente2.adicionarConsulta("Consulta de emergência - 02/09/2024");

paciente1.verHistorico();

paciente2.verHistorico();
