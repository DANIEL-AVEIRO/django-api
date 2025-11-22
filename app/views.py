from django.shortcuts import render
from app.models import ProductModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def product_list(request):
    products = ProductModel.objects.all()
    return Response(
        {
            "success": True,
            "message": "Product retrieved successfully",
            "products": [
                {
                    "name": product.name,
                    "price": product.price,
                    "created_at": product.created_at,
                    "updated_at": product.updated_at,
                }
                for product in products
            ],
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def product_create(request):
    try:
        name = request.data.get("name")
        price = request.data.get("price")
        if not name and not price:
            return Response(
                {
                    "success": False,
                    "message": "All fields are required",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        product = ProductModel.objects.create(name=name, price=price)
        product.save()
        return Response(
            {
                "success": True,
                "message": "Product create successfully",
                "product": {
                    "name": product.name,
                    "price": product.price,
                    "created_at": product.created_at,
                    "updated_at": product.updated_at,
                },
            },
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response(
            {
                "success": False,
                "message": f"Error {str(e)}",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PUT"])
def product_update(request, pk):
    product = ProductModel.objects.get(id=pk)
    if not product:
        return Response(
            {
                "success": False,
                "message": "Product not found",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    name = request.data.get("name")
    price = request.data.get("price")
    if not name and not price:
        return Response(
            {
                "success": False,
                "message": "All fields are required",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    product.name = name
    product.price = price
    product.save()
    return Response(
        {
            "success": True,
            "message": "Product updated successfully",
            "product": {
                "name": product.name,
                "price": product.price,
                "created_at": product.created_at,
                "updated_at": product.updated_at,
            },
        },
        status=status.HTTP_200_OK,
    )


@api_view(["DELETE"])
def product_delete(request, pk):
    product = ProductModel.objects.get(id=pk)
    if not product:
        return Response(
            {
                "success": False,
                "message": "Product not found",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    product.delete()
    return Response(
        {
            "success": True,
            "message": "Product delete successfully",
        },
        status=status.HTTP_200_OK,
    )
