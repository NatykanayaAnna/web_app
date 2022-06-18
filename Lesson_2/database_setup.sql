create database banners_project;
create user banner_admin with encrypted password 'postgres';
grant all privileges on database banners_project to banner_admin;
\c banners_project;

