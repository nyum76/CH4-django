from django import forms
from .models import Product, HashTag

class ProductForm(forms.ModelForm):
    hashtags_str = forms.CharField(required=False)
    
    # 상품 폼을 생성할 때 중요한건 사용자!! -> 누가 이 상품을 등록하는가가 중요함
    # 사용자를 가져와서 해당 상품이랑 연결시켜주기~
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) # user 인자를 가져오고 없으면 None 을 반환
        super().__init__(*args, **kwargs) # 부모 클래스 초기화
        
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'hashtags_str']
        
        
    # save 메서드 -  폼에서 입력한 데이터를 db에 저장
    def save(self, commit=True): # 커밋트루 - 바로 적용
        # 부모 클래스의 save 메서드를 호출하되, commit=False -> 해당 상품은 들고오지만 db에 저장은 안 함
        # 1. product 객체를 생성하고, 추가 작업 (해시태그 처리)을 완료한 후 commit (db에 반영)
        # 2. user와 연결을 시켜줘야함. 그 결과를 db 에 적재하기 위해 일단 commit=False
        product = super().save(commit=False)
        
        if self.user:
            product.user = self.user
            
        if commit:
            product.save()
            
        # 해시태그 처리
        # 입력 받은 hashtag_str 문자열을 쉼표나 공백으로 구분 (제한)
        # 각 해시태그를 db ㅇㅔ 저장하거나, 이미 존재하면 가져옴
        hashtags_input = self.cleaned_data.get('hashtags_str','')
        hashtag_list = [ h for h in hashtags_input.replace(',', '').split() if h]
        new_hashtags = []
        for ht in hashtag_list:
            ht_obj, created = HashTag.objects.get_or_create(name=ht)
            new_hashtags.append(ht_obj)
        
        # 다대다 관계 설정
        product.hashtags.set(new_hashtags)
        
        if not commit:
            product.save()
            
        return product