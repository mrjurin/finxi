import uuid
from django.shortcuts import resolve_url as r
from django.db import models

# Transaction Types
from accounts.models import User

SELL = 'S'
RENT = 'R'
ANY = 'A'

# Real Estate Types
LAND = 'L'
HOUSE = 'H'
APARTMENT = 'A'
FLAT = 'F'
PENTHOUSE = 'P'
KITNET = 'K'


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField('Endereço', max_length=255)
    number = models.CharField('Número', max_length=5, blank=True, null=True)
    city = models.ForeignKey('catalog.City', verbose_name='Cidade')
    postal_code = models.CharField('CEP', max_length=10, blank=True, null=True)
    neighborhood = models.CharField('Bairro', max_length=30)

    def __str__(self):
        return "{}, {} - {}/{} ".format(self.street, self.number, self.city.name, self.city.state.abbreviation)


class RealEstate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    TYPES = (
        (LAND, 'Terreno'),
        (HOUSE, 'Casa'),
        (APARTMENT, 'Apartamento'),
        (FLAT, 'Flat'),
        (PENTHOUSE, 'Terreno'),
        (KITNET, 'Kitnet'),
    )
    type = models.CharField('Tipo', max_length=1, choices=TYPES)

    TRANSACTION_TYPES = (
        (SELL, 'Venda'),
        (RENT, 'Aluguel'),
        (ANY, 'Venda ou Aluguel')
    )
    transaction_type = models.CharField('Tipo de Operação', max_length=1, choices=TRANSACTION_TYPES)

    address = models.ForeignKey(Address, related_name='address')
    # seller = models.ForeignKey(User, related_name='seller', verbose_name='Anunciante')

    title = models.CharField('Título', max_length=50)
    description = models.TextField('Descrição')
    sell_price = models.DecimalField('Venda', decimal_places=2, max_digits=10, null=True, blank=True)
    rent_price = models.DecimalField('Aluguel', decimal_places=2, max_digits=8, null=True, blank=True)
    area = models.IntegerField('Área')
    tax = models.DecimalField('IPTU', decimal_places=2, max_digits=8, null=True, blank=True)
    condo_price = models.DecimalField('Condomínio', decimal_places=2, max_digits=8, null=True, blank=True)
    number_of_rooms = models.IntegerField('Quartos')
    number_of_bathrooms = models.IntegerField('Banheiros')
    number_of_suites = models.IntegerField('Suítes')
    number_of_car_parks = models.IntegerField('Vagas')
    sold = models.BooleanField('Vendido', default=False)
    sold_at = models.DateTimeField('Vendido em', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('show_real_estate', real_estate_id=self.id)


# ToDo: Características: mobiliado, churrasqueira, espaço gourmet, etc..
# ToDo: Upload de Imagens
# class Photo(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
#     path = models.CharField(max_length=255)
#     default = models.BooleanField(default=False)


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    code = models.CharField('DDD', max_length=5)
    number = models.CharField('Número', max_length=20)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return "{}-{}".format(self.code, self.number)


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=80)
    slug = models.SlugField('Slug', unique=True)
    state = models.ForeignKey('catalog.State', verbose_name='Estado')
    capital = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_search_url(self):
        return r('list_real_state_buy_param', state=self.state.abbreviation.lower(), slug=self.slug)


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=50)
    abbreviation = models.CharField('UF', max_length=2, unique=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['name']

    def __str__(self):
        return self.name
