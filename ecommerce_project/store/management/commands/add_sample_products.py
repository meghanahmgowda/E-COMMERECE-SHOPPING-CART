from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Add 100 sample products'

    def handle(self, *args, **kwargs):
        for i in range(1, 101):
            Product.objects.get_or_create(
                name=f"Ladies Dress {i}",
                description=f"Elegant Ladies Dress number {i}",
                price=round(500 + i*2.5, 2),
                image_url=f"https://picsum.photos/seed/dress{i}/400/400"
            )
        self.stdout.write(self.style.SUCCESS('Successfully added 100 sample products!'))
