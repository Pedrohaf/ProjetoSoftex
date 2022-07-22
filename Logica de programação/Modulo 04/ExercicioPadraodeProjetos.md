# Abstract Factory
A intenção deste é fornecer uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. Também é conhecido como Kit.

Este padrão deve ser aplicado quando se deseja isolar a aplicação da implementação da classe concreta, que poderia ser um componente e ou framework específico no qual a aplicação conheceria apenas uma interface e a implementação concreta seria conhecida apenas em tempo de execução ou compilação.

# De acordo com o exposto pelos quatro amigos, o uso do padrão Abstract Factory deve estar restrito as seguintes situações:
- Um sistema deve ser independente de como seus produtos são criados, compostos ou representados;
- Um sistema deve ser configurado como um produto de uma família de múltiplos produtos;
- Uma família de objetos for projetada para ser usada em conjunto, e você necessita garantir esta restrição;
- Você quer fornecer uma biblioteca de classes de produtos e quer revelar somente suas interfaces, não suas   implementações.