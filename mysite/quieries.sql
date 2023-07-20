select "shopapp_product"."id",
        "shopapp_product"."name",
        "shopapp_product"."description",
        "shopapp_product"."price",
        "shopapp_product"."discount",
        "shopapp_product"."created_at",
        "shopapp_product"."archived",
        "shopapp_product"."preview"
from "shopapp_product"
where not "shopapp_product"."archived";

SELECT name, type FROM sqlite_master
WHERE type in ('table', 'view') AND NOT name='sqlite_sequence'
ORDER BY name;

SELECT "django_migrations"."id",
        "django_migrations"."app",
        "django_migrations"."name",
        "django_migrations"."applied"
FROM "django_migrations";


SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date"
FROM "django_session"
WHERE ("django_session"."expire_date" > '2023-06-27 11:17:13.706437' AND "django_session"."session_key" = '1rp30mchp1i9wtcv414c4wtfghewqrwa')
LIMIT 21; args=('2023-06-27 11:17:13.706437', '1rp30mchp1i9wtcv414c4wtfghewqrwa');

SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "auth_user"
WHERE "auth_user"."id" = 1
LIMIT 21;

SELECT "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode", "shopapp_order"."created_at", "shopapp_order"."user_id", "shopapp_order"."receipt", "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"
FROM "shopapp_order"
INNER JOIN "auth_user" ON ("shopapp_order"."user_id" = "auth_user"."id");

SELECT ("shopapp_order_products"."order_id")
AS "_prefetch_related_val_order_id", "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp_product"."created_at", "shopapp_product"."archived", "shopapp_product"."preview"
FROM "shopapp_product"
INNER JOIN "shopapp_order_products"
ON ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE "shopapp_order_products"."order_id" IN (1, 3);
