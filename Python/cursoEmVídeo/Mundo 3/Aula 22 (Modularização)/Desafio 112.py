from utilidadesCeV import dado, moeda

preço = dado.lerNúmero('Digite o preço: \033[032mR$', 'Digite somente valores monetários por favor!')
moeda.mostrarPreçoComAlterações(preço, 80, 30)