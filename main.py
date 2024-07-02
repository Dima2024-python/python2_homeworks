# from fastapi import FastAPI, HTTPException, Query, Request
# from fastapi.params import Path
# from fastapi.templating import Jinja2Templates
# from starlette import status
#
# import config
# import dao
# from database import create_tables
# from schemas import CreatedProduct
#
# templates = Jinja2Templates(directory="templates")
#
#
# # @contextmanager
# def lifespan(app: FastAPI):
#     create_tables()
#     yield
#
#
# app = FastAPI(debug=config.DEBUG, lifespan=lifespan)
#
#
# @app.post("/api/products/create/", status_code=status.HTTP_201_CREATED, tags=["API", "Products"])
# def crete_product(new_product: NewProduct) -> CreatedProduct:
#     print(new_product.dict())
#     created_product = dao.create_product(**new_product.dict())
#     return created_product
#
#
# @app.get("/api/products/", tags=["API", "Products"])
# def get_products(
#     limit: int = Query(default=5, gt=0, le=50, description="Number of products"),
#     skip: int = Query(default=5, ge=0, description="How many to skip"),
#     name: str = Query(default="", description="Part of the product name"),
# ) -> list[CreatedProduct]:
#     products = dao.get_all_products(limit=limit, skip=skip, name=name)
#     return products
#
#
# @app.get("/api/products/{product_id}", tags=["API", "Products"])
# def get_product(product_id: int = Path(gt=0, description="Number of product")) -> CreatedProduct:
#     products = dao.get_all_product_by_id(product_id=product_id)
#     if products:
#         return products
#     raise HTTPException(status_code=404, detail="Not found")
#
#
# @app.put("/api/products/{product_id}", tags=["API", "Products"])
# def update_product(
#     updated_product: NewProduct, product_id: int = Path(gt=0, description="Number of product")
# ) -> CreatedProduct:
#     products = dao.get_all_product_by_id(product_id=product_id)
#     if not products:
#         raise HTTPException(status_code=404, detail="Not found")
#
#     products = dao.update_product(product_id, **updated_product.dict())
#     return products
#
#
# @app.delete("/api/products/{product_id}", tags=["API", "Products"])
# def delete_product(product_id: int = Path(gt=0, description="Number of product")) -> DeletedProduct:
#     products = dao.get_all_product_by_id(product_id=product_id)
#     if not products:
#         raise HTTPException(status_code=404, detail="Not found")
#     dao.delete_product(product_id=product_id)
#     return DeletedProduct(id=product_id)
#
#
# @app.get("/", include_in_schema=False)
# def index_web(request: Request):
#
#     return templates.TemplateResponse("index.html", {"request": request, "books": {}, "title": "Main page"})
