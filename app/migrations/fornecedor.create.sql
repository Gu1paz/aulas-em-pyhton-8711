use mini_erp;

create table fornecedor
(
	id integer not null auto_increment primary key, 
    razao_social varchar(55) not null, 
    nome_fantasia varchar(55) not null, 
    cnpj varchar(18) not null unique, 
    sla_atendimento integer not null
);
