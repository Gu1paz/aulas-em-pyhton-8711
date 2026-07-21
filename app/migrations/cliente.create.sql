use mini_erp;

create table cliente
(
	id integer not null auto_increment primary key, 
    nome varchar(50) not null, 
    data_nascimento date not null, 
    limite_credito decimal(10,2) not null default 0.00
);