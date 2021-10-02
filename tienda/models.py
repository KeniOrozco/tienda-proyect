from django.db import models
from django.contrib.auth import get_user_model
#Elementos de la tienda 

Usuario = get_user_model()
class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    class Meta:
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.nombre

class Producto(models.Model): 
    titulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='producto_imagen')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=False)
    categoria_p = models.ForeignKey(Categoria, related_name='productos_p', on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse("tienda:producto-detail", kwargs={'slug_name': self.slug_name})
    @property
    def en_stock(self):
        return self.stock > 5

class Direccion(models.Model): 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=150) 
    referencia = models.CharField(max_length=150) 
    ciudad = models.CharField(max_length=150) 
    PAIS= [
        ('0', 'GUATEMALA'),
     ]
    pais = models.IntegerField(choices=PAIS, null=False, blank=False)
    REGION= [ 
        ('0', 'Alta Verapaz'),
        ('1', 'Baja Verapaz'),
        ('2', 'Chimaltenago'),
        ('3', 'Chiquimula'),
        ('4', 'Guatemala'),
        ('5', 'El Progreso'),
        ('6', 'Escuintla'),
        ('7', 'Huehuetenango'),
        ('8', 'Izabal'),
        ('9', 'Jalapa'),
        ('10', 'Jutiapa'),
        ('11', 'Petén'),
        ('12', 'Quetzaltenango'),
        ('13', 'Quiché'),
        ('14', 'Retalhuleu'),
        ('15', 'Sacatepequez'),
        ('16', 'San Marcos'),
        ('17', 'Santa Rosa'),
        ('18', 'Sololá'),
        ('19', 'Suchitepequez'),
        ('20', 'Totonicapán'),
        ('21', 'Zacapa'),
    ]
    region = models.IntegerField(choices=REGION, null=False, blank=False)
    zipcode = models.CharField(max_length=6) 

    def __str__(self):
        txt="{0} {1} {2} {3}"
        return txt.format(self.direccion, self.referencia, self.ciudad, self.zipcode ) 

    class Meta:
        verbose_name_plural = 'Direcciones'

class OrdenItem(models.Model):
  
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default = 1)

    def __str__(self):
        txt="{0} {1}"
        return txt.format (self.cantidad, self.producto.titulo) 
    

    def precio_previo(self):
        return self.cantidad * self.producto.precio

    def total_por_item(self):
        price  = self.precio_previo() #1000
        return "{:.2f}".format(price / 100)


class Orden(models.Model):
    usuario = models.ForeignKey(
        Usuario,blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    fecha_orden = models.DateTimeField(blank=True, null=True)
    status_orden = models.BooleanField(default=False)
    direccion_envio = models.ForeignKey(Direccion, related_name='direccion_envio', blank=True, null=True, on_delete=models.SET_NULL)
   

    def __str__(self):
        return self.no_referencia

    @property
    def no_referencia(self):
        return f"ORDEN-{self.pk}"

    def get_subtotal(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.total_por_item()
        return total

    def get_subtotal(self):
        subtotal = self.get_subtotal()
        return "{:.2f}".format(subtotal / 100)

    def get_total(self):
        subtotal = self.get_subtotal()
        return subtotal

    def get_total(self):
        total = self.get_total()
        return "{:.2f}".format(total / 100)