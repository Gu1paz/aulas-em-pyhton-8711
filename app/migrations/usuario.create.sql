use mini_erp;

create table usuario
(
	id integer not null auto_increment primary key, 
    nome varchar(50) not null, 
    email varchar(50) not null, 
    data_nascimento date not null
);
