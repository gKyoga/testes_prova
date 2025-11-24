from sistema_pedidos import buscar_detalhes_pedido

def test_access_to_foreign_order_must_be_denied():
    user_id = 2
    order_id = 2

    output = buscar_detalhes_pedido(order_id, user_id)

    assert output == {}, "Violação de segurança: acesso não autorizado ao pedido deve ser devolvido."

