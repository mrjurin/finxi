import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField('Endereço', max_length=255)
    number = models.CharField('Número', max_length=5, blank=True, null=True)
    city = models.ForeignKey('catalog.City', verbose_name='Cidade')
    postalCode = models.CharField('CEP', max_length=10, blank=True, null=True)
    neighborhood = models.CharField('Bairro', max_length=30)

    def __str__(self):
        return "{}, {} - {}/{} ".format(self.street, self.number, self.city.name, self.city.state.abbreviation)


class RealEstate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    LAND = 'L'
    HOUSE = 'H'
    APARTMENT = 'A'
    FLAT = 'F'
    PENTHOUSE = 'P'
    KITNET = 'K'
    TYPES = (
        (LAND, 'Terreno'),
        (HOUSE, 'Casa'),
        (APARTMENT, 'Apartamento'),
        (FLAT, 'Flat'),
        (PENTHOUSE, 'Terreno'),
        (KITNET, 'Kitnet'),
    )
    type = models.CharField('Tipo', max_length=1, choices=TYPES)

    SELL = 'S'
    RENT = 'R'
    ANY = 'A'
    TRANSACTION_TYPES = (
        (SELL, 'Venda'),
        (RENT, 'Aluguel'),
        (ANY, 'Venda ou Aluguel')
    )
    transactionType = models.CharField('Tipo de Operação', max_length=1, choices=TRANSACTION_TYPES)
    address = models.OneToOneField(
        Address,
        on_delete=None,
        verbose_name='Localização'
    )

    seller = models.ForeignKey('catalog.Seller', verbose_name='Anunciante')
    title = models.CharField(max_length=255)
    description = models.TextField()
    sellPrice = models.DecimalField('Preço de Venda', decimal_places=2, max_digits=10, null=True, blank=True)
    rentPrice = models.DecimalField('Aluguel', decimal_places=2, max_digits=8, null=True, blank=True)
    area = models.IntegerField('Área')
    tax = models.DecimalField('IPTU', decimal_places=2, max_digits=8, null=True, blank=True)
    condoPrice = models.DecimalField('Condomínio', decimal_places=2, max_digits=8, null=True, blank=True)
    numberOfRooms = models.IntegerField('Quartos')
    numberOfBathrooms = models.IntegerField('Banheiros')
    numberOfSuites = models.IntegerField('Suítes')
    numberOfCarParks = models.IntegerField('Vagas de Garagem')
    sold = models.BooleanField('Vendido', default=False)
    sold_at = models.DateTimeField('Vendido em', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self):
        return self.title


# ToDo: Características: mobiliado, churrasqueira, espaço gourmet, etc..
# ToDo: Upload de Imagens
# class Photo(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
#     path = models.CharField(max_length=255)
#     default = models.BooleanField(default=False)


class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField('Nome', max_length=100)
    surname = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email')

    class Meta:
        verbose_name = 'Anunciante'
        verbose_name_plural = 'Anunciantes'

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


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
    state = models.ForeignKey('catalog.State', verbose_name='Estado')
    capital = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']

    def __str__(self):
        return self.name


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
