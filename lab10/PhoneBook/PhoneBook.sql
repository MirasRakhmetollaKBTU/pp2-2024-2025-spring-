PGDMP  6    0        
        }         	   PhoneBook    17.4    17.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16388 	   PhoneBook    DATABASE     q   CREATE DATABASE "PhoneBook" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru-RU';
    DROP DATABASE "PhoneBook";
                     postgres    false            �            1259    16390 	   phonebook    TABLE     �   CREATE TABLE public.phonebook (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    number character varying(15) NOT NULL
);
    DROP TABLE public.phonebook;
       public         heap r       postgres    false            �            1259    16389    phonebook_id_seq    SEQUENCE     �   CREATE SEQUENCE public.phonebook_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.phonebook_id_seq;
       public               postgres    false    218            �           0    0    phonebook_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.phonebook_id_seq OWNED BY public.phonebook.id;
          public               postgres    false    217            W           2604    16393    phonebook id    DEFAULT     l   ALTER TABLE ONLY public.phonebook ALTER COLUMN id SET DEFAULT nextval('public.phonebook_id_seq'::regclass);
 ;   ALTER TABLE public.phonebook ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218            �          0    16390 	   phonebook 
   TABLE DATA           5   COPY public.phonebook (id, name, number) FROM stdin;
    public               postgres    false    218   �
       �           0    0    phonebook_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.phonebook_id_seq', 6, true);
          public               postgres    false    217            Y           2606    16395    phonebook phonebook_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.phonebook
    ADD CONSTRAINT phonebook_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.phonebook DROP CONSTRAINT phonebook_pkey;
       public                 postgres    false    218            �   R   x��;
�0 �9�� ��ttu��5��}�#��s�0����(��(f�Ƃ
K�D�&!4h=�|!�����p��[�     