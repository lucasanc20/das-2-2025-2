# das-2-2025-2


- Aula 30/07

Well-Architected Framework: Um guia da AWS para construir sistemas na nuvem de forma sólida. Ele se concentra em cinco pontos-chave: segurança, velocidade, confiabilidade, economia e organização.

Trade-offs: Em arquitetura, é a arte de escolher. Você não pode ter tudo, então precisa decidir o que é mais importante, como trocar um pouco de performance por um custo menor.


- Aula 06/08

Responsabilidade Compartilhada: A segurança na AWS é um trabalho em equipe. A AWS cuida da segurança da nuvem (a infraestrutura física), e você cuida da segurança na nuvem (suas configurações e dados).

Privilégio Mínimo: Conceda o mínimo de permissões possível. Dê a um usuário ou serviço apenas o que ele precisa para trabalhar, e nada mais.

Autenticação e Autorização: Autenticação é o ato de provar quem você é. Autorização é o que você pode fazer depois de provar sua identidade.

IAM User vs. IAM Role: Pense no IAM User como sua identidade pessoal para acessar a AWS. O IAM Role é uma "identidade temporária" que você pode assumir para ter acesso a algo sem precisar de credenciais fixas.


- Aula 13/08

Políticas de Permissão:

Identity-Based Policies: Permissões anexadas a uma identidade, como um usuário ou grupo.

Resource-Based Policies: Permissões anexadas diretamente a um recurso, como um bucket do S3.


- Aula 20/08

Tipos de Armazenamento:

Block Storage: Perfeito para sistemas operacionais e bancos de dados que precisam de acesso super-rápido.

File Share: Para quando várias pessoas ou aplicativos precisam acessar o mesmo arquivo ao mesmo tempo.

Object Store: Armazena fotos, vídeos, logs e outros dados que não precisam de uma estrutura rígida. É ótimo para armazenar grandes volumes de dados.

S3: O serviço de armazenamento de objetos da AWS. É conhecido por ser super confiável e escalável, ideal para backups, sites estáticos e muito mais.


- Aula 27/08

S3: Mais que arquivos: O S3 não armazena apenas arquivos; ele armazena objetos, que são arquivos com informações extras (metadados).

Bucket: Onde você armazena seus objetos no S3. É como uma pasta, mas com algumas regras especiais.

Escolhendo a Região: A região do bucket é importante. Pense na proximidade dos seus usuários, nas leis de dados locais, no custo e nos serviços disponíveis.

Inventário do S3: Uma ferramenta que te dá uma lista detalhada de tudo o que está no seu bucket, ajudando na organização e auditoria.


- Aula 03/09

Serviços Computacionais: Onde você roda suas aplicações na nuvem.

EC2: Alugue servidores virtuais da AWS para rodar o que você quiser. Você tem controle total.

AMI: Uma "foto" de um servidor pré-configurado, pronta para ser usada. Ela já vem com sistema operacional e softwares instalados.

Tipos de Instâncias: As instâncias EC2 são classificadas por famílias, cada uma otimizada para uma tarefa diferente (ex: processamento, memória, etc.).

EBS vs. Instance Store:

EBS: Armazenamento que persiste. Se você desligar o servidor, seus dados ainda estarão lá.

Instance Store: Armazenamento temporário. Os dados são apagados quando o servidor desliga.

Acesso a Servidores:

SSH: Para se conectar a servidores Linux.

RDP: Para se conectar a servidores Windows.


- Aula 10/09

EFS vs. FSx:

EFS: Sistema de arquivos que pode ser compartilhado por vários servidores EC2.

FSx: Permite usar sistemas de arquivos específicos como os do Windows ou Lustre, facilitando a migração.

EC2 Windows: Você também pode rodar servidores virtuais com o sistema operacional Windows na AWS.


- Aula 17/09

EC2: O serviço que te dá servidores virtuais flexíveis e escaláveis na nuvem.

User Data: Um script que roda automaticamente na inicialização do servidor. Ótimo para automatizar tarefas.

Instance Metadata: Informações sobre o servidor que podem ser acessadas de dentro dele.

Placement: Decide onde seus servidores serão fisicamente colocados para otimizar a performance.

VPC: Sua rede privada virtual na AWS, isolada de todo o resto.

Subnets (Públicas e Privadas):

Pública: Conectada à internet.

Privada: Isolada da internet.

Segurança de Rede:

Security Group: Um firewall para o servidor.

NACL: Um firewall para a sub-rede.

Conectando redes:

VPN Site-to-Site: Conecta sua rede local à sua rede na AWS.

Peering: Conecta duas redes da AWS entre si.
