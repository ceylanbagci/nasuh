"""
Django ORM ile veritabanı işlemlerini gerçekleştirirken kullanılan yardımcı fonksiyolardır.
param model_class: Modelin sınıf adıdır.
param **kwargs: İlgili modelde filtreleme yapmak için kullanılan sözlük verisidir.
"""
def get_or_none(model_class, **kwargs):
    try:
        return model_class.objects.get(**kwargs)
    # TODO bunu bilerek genel yaptım exam da boş gelen verilerde başka yerde kontrol yapmak yerine
    # except model_class.DoesNotExist:
    except Exception as e:
        return None

def get_none(model_class):
    try:
        return model_class.objects.none()
    except model_class.DoesNotExist:
        return None

def get_last(model_class,**kwargs):
    try:
        return model_class.objects.filter(**kwargs).last()
    except model_class.DoesNotExist:
        return None

def get_list(model_class,**kwargs):
    try:
        return model_class.objects.filter(**kwargs).order_by("-id")
    except model_class.DoesNotExist:
        return None

def get_list_part(model_class, start, end,**kwargs):
    try:
        return model_class.objects.filter(**kwargs).order_by("-id")[start:end]
    except model_class.DoesNotExist:
        return None

def get_count(model_class,**kwargs):
    try:
        return model_class.objects.filter(**kwargs).count()
    except model_class.DoesNotExist:
        return 0

def custom_create(model_class,**kwargs):
    try:
        return model_class.objects.create(**kwargs)
    except Exception as e:
        return None

def custom_update(model_class,id,parameters):
    try:
        obj = model_class.objects.get(id=id)
        for key in parameters:
            setattr(obj, key, parameters[key])
        obj.save()
        return obj
    # except model_class.DoesNotExist:
    except Exception as e:
        return None

def custom_delete(model_class,**kwargs):
    try:
        model_class.objects.filter(**kwargs).delete()
        return True
    except model_class.DoesNotExist:
        return False

def delete_object(model_class,**kwargs):
    try:
        obj = model_class.objects.get(**kwargs)
        obj.delete()
        return True
    except model_class.DoesNotExist:
        return False

def any(model_class,**kwargs):
    try:
        return model_class.objects.filter(**kwargs).exists()
    except Exception as e:
        return False
